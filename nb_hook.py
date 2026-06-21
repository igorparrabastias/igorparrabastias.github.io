"""
Hook de MkDocs que integra TODOS los notebooks de notebook/ sin tocarlos:

  1. on_config  -> copia notebook/ dentro de pages/notebook/ (gitignored) para
                   que mkdocs-jupyter los descubra y renderice, y arma la
                   navegación lateral "Notebooks (ejecutables)" agrupada por
                   carpeta (sin listarlos a mano en mkdocs.yml).
  2. on_page_content -> inyecta el botón "Abrir en Colab" arriba de cada
                   notebook renderizado. Cero ediciones dentro de los .ipynb.

Las URLs de Colab/GitHub apuntan a notebook/<...> en master (su ubicación real
en el repo); la copia en pages/ es solo para el build y no se commitea.
"""
import os
import sys
import json
import glob
import shutil

REPO = os.path.dirname(os.path.abspath(__file__))
# Orden pedagógico real de los notebooks (generado por _gen_nb_order.py desde los
# índices curados). Sin esto, el menú saldría en orden alfabético y rompería la
# secuencia de estudio.
sys.path.insert(0, REPO)
try:
    from nb_order import ORDER
except Exception:
    ORDER = {}
SRC = os.path.join(REPO, "notebook")
DOCS = os.path.join(REPO, "docs")
DST = os.path.join(DOCS, "notebook")
GH = "igorparrabastias/igorparrabastias.github.io"
BRANCH = "main"


def _titulo(slug):
    return slug.replace("-", " ").replace("_", " ").strip().capitalize()


def on_config(config):
    # Modo rápido para desarrollo: NB_SKIP=1 mkdocs serve  -> omite los ~263
    # notebooks (lo más lento del build) para iterar prosa sin esperar minutos.
    if os.environ.get("NB_SKIP"):
        if os.path.isdir(DST):
            shutil.rmtree(DST)
        print("nb_hook: NB_SKIP activo -> notebooks omitidos (modo rápido).")
        return config

    # Copia fresca de los notebooks dentro de docs_dir para que mkdocs-jupyter
    # los descubra (solo escanea docs_dir). docs/notebook/ está en .gitignore.
    if os.path.isdir(DST):
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    # Descarta notebooks vacíos o con JSON inválido (romperían mkdocs-jupyter).
    descartados = []
    for p in glob.glob(os.path.join(DST, "**", "*.ipynb"), recursive=True):
        try:
            with open(p, encoding="utf-8") as fh:
                json.load(fh)
        except Exception:
            os.remove(p)
            descartados.append(os.path.relpath(p, DST))
    if descartados:
        print("nb_hook: notebooks omitidos (vacíos/corruptos): " + ", ".join(descartados))

    # Navegación agrupada por carpeta, RESPETANDO el orden pedagógico de ORDER.
    # Lo listado en el índice curado va primero (en ese orden); lo no listado va
    # después, alfabético. Nunca alfabético "a secas" (rompería el orden de estudio).
    crudos = {}
    for p in glob.glob(os.path.join(DST, "**", "*.ipynb"), recursive=True):
        uri = os.path.relpath(p, DOCS).replace(os.sep, "/")
        partes = uri.split("/")          # notebook / carpeta / [...] / archivo.ipynb
        carpeta = partes[1] if len(partes) > 2 else "(raíz)"
        stem = os.path.splitext(partes[-1])[0]
        crudos.setdefault(carpeta, []).append((stem, uri))

    def _rank(carpeta, stem):
        seq = ORDER.get(carpeta, [])
        return (seq.index(stem), "") if stem in seq else (len(seq), stem)

    grupos = {}
    for carpeta, lst in crudos.items():
        lst.sort(key=lambda t: _rank(carpeta, t[0]))
        grupos[carpeta] = [{_titulo(s): u} for s, u in lst]

    # Temática primero: cada carpeta de notebooks se ANIDA bajo su sección del nav
    # (las secciones existen en mkdocs.yml). El lenguaje/implementación va dentro.
    THEMES = {
        "Fundamentos de Python": [
            "python-repaso-basico", "python-repaso-avanzado", "anexos",
        ],
        "Estructuras de datos": [
            "estructuras-de-datos-nativas-de-python",
            "implementacion-de-estructuras-de-datos-en-python",
            "implementacion-de-estructuras-simples",
            "arboles", "implementacion-de-arboles",
            "implementacion-de-tablas-hash",
            "implementacion-de-heaps",
            "estructuras-de-datos-avanzadas",
        ],
        "Algoritmos": [
            "algoritmos-basicos-de-ordenamiento",
            "algoritmos-basicos-de-busqueda",
            "algoritmos-de-grafos",
            "algoritmos-de-grafos-recorrido-de-grafos",
            "algoritmos-de-grafos-otras-aplicaciones",
            "implementacion-de-grafos",
        ],
        "Matemáticas y teoría": [
            "habilidades-de-resolucion-de-problemas-tecnicas-de-analisis-de-problemas",
            "habilidades-de-resolucion-de-problemas-complejidad-algoritmica-y-optimizacion",
            "transicion-a-experto-matematicas-y-teoria-detras-de-los-algoritmos",
        ],
    }
    NICE = {
        "estructuras-de-datos-nativas-de-python": "Estructuras nativas de Python",
        "implementacion-de-estructuras-de-datos-en-python": "Implementación en Python",
        "implementacion-de-estructuras-simples": "Estructuras simples (listas, pilas, colas)",
        "implementacion-de-tablas-hash": "Tablas hash",
        "implementacion-de-heaps": "Heaps",
        "estructuras-de-datos-avanzadas": "Estructuras avanzadas",
        "implementacion-de-arboles": "Implementación de árboles",
        "arboles": "Árboles",
        "algoritmos-basicos-de-busqueda": "Búsqueda",
        "algoritmos-basicos-de-ordenamiento": "Ordenamiento",
        "algoritmos-de-grafos": "Grafos · algoritmos",
        "algoritmos-de-grafos-recorrido-de-grafos": "Grafos · recorridos (DFS/BFS)",
        "algoritmos-de-grafos-otras-aplicaciones": "Grafos · aplicaciones",
        "implementacion-de-grafos": "Grafos · implementación",
        "python-repaso-basico": "Python · repaso básico",
        "python-repaso-avanzado": "Python · repaso avanzado",
        "anexos": "Anexos",
        "habilidades-de-resolucion-de-problemas-complejidad-algoritmica-y-optimizacion":
            "Complejidad algorítmica y optimización",
        "habilidades-de-resolucion-de-problemas-tecnicas-de-analisis-de-problemas":
            "Técnicas de análisis de problemas",
        "transicion-a-experto-matematicas-y-teoria-detras-de-los-algoritmos":
            "Teoría detrás de los algoritmos",
    }
    # Subgrupo por carpeta, repartido por tema RESPETANDO el orden de THEMES
    # (no alfabético: así el sidebar sigue el mismo orden que las páginas-índice).
    entries = {c: {NICE.get(c, _titulo(c)): grupos[c]} for c in grupos}
    por_tema, leftover, asignadas = {}, [], set()
    for t, folders in THEMES.items():
        for c in folders:
            if c in entries:
                por_tema.setdefault(t, []).append(entries[c])
                asignadas.add(c)
    for c in sorted(entries):                 # carpetas no mapeadas, al final
        if c not in asignadas:
            leftover.append(entries[c])

    def _inject(nav, title, items):
        for node in nav:
            if isinstance(node, dict):
                for k, v in node.items():
                    if k == title and isinstance(v, list):
                        # Inserta los notebooks DESPUÉS del índice de la sección
                        # (las páginas iniciales que son str), antes de los
                        # subgrupos (dicts, p.ej. "JavaScript"). Así el menú
                        # coincide con el orden de la página y el lenguaje queda
                        # anidado al final.
                        pos = 0
                        while pos < len(v) and not isinstance(v[pos], dict):
                            pos += 1
                        v[pos:pos] = items
                        return True
                    if isinstance(v, list) and _inject(v, title, items):
                        return True
        return False

    for t, items in por_tema.items():
        if not _inject(config["nav"], t, items):
            leftover.extend(items)
    if leftover:
        config["nav"].append({"Más notebooks": leftover})
    return config


def on_page_content(html, page, config, files):
    src = page.file.src_uri
    if not src.endswith(".ipynb"):
        return html
    # src es 'notebook/<...>.ipynb' (o 'demo/slicing.ipynb'); ambos existen en master.
    colab = f"https://colab.research.google.com/github/{GH}/blob/{BRANCH}/{src}"
    github = f"https://github.com/{GH}/blob/{BRANCH}/{src}"
    boton = (
        '<p>'
        f'<a class="md-button md-button--primary" target="_blank" href="{colab}">'
        '▶ Abrir en Colab</a> '
        f'<a class="md-button" target="_blank" href="{github}">Ver en GitHub</a>'
        '</p>'
    )
    return boton + html
