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
import re
import sys
import json
import glob
import shutil

try:
    from mkdocs.utils import get_relative_url
except Exception:                       # pragma: no cover
    get_relative_url = None

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
        # Matemáticas: cada carpeta cuelga de su propia sub-página (ver mkdocs.yml),
        # no de un único "Matemáticas y teoría". Así las cards del índice coinciden
        # con el sidebar y cada una lleva a su página.
        "Técnicas de análisis de problemas": [
            "habilidades-de-resolucion-de-problemas-tecnicas-de-analisis-de-problemas",
        ],
        "Complejidad algorítmica y optimización": [
            "habilidades-de-resolucion-de-problemas-complejidad-algoritmica-y-optimizacion",
        ],
        "Teoría detrás de los algoritmos": [
            "transicion-a-experto-matematicas-y-teoria-detras-de-los-algoritmos",
        ],
        "Problemas de Estructuras de Datos y Algoritmos": [
            "problemas-de-estructuras-y-algoritmos",
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
        "problemas-de-estructuras-y-algoritmos": "Ejercicios resueltos (Python)",
    }
    # Subgrupo por carpeta, repartido por tema RESPETANDO el orden de THEMES
    # (no alfabético: así el sidebar sigue el mismo orden que las páginas-índice).
    entries = {c: {NICE.get(c, _titulo(c)): grupos[c]} for c in grupos}
    por_tema, leftover, asignadas = {}, [], set()
    for t, folders in THEMES.items():
        present = [c for c in folders if c in entries]
        for c in present:
            asignadas.add(c)
        if len(present) == 1:
            # Tema de una sola carpeta: cuelga los notebooks DIRECTAMENTE de la
            # sección (sin un sub-grupo cuyo nombre duplicaría el de la sección).
            por_tema[t] = list(grupos[present[0]])
        elif present:
            por_tema[t] = [entries[c] for c in present]
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


# Enlaces internos heredados: los notebooks de 'problemas' venían de problems/ (raíz
# del repo) con rutas '../notebook/...' que, al renderizarse ahora en notebook/<carpeta>/,
# resuelven a /notebook/notebook/... (doble). Se corrige la base ('../notebook/' -> '../')
# y se apunta al .html renderizado. Algunos destinos cambiaron de nombre al unificar el
# repo; se remapean a su equivalente actual para que no queden enlaces rotos.
_NB_REMAP = {
    "implementacion-de-estructuras-simples/linked-lists-listas-enlazadas":
        "implementacion-de-estructuras-simples/listas-enlazadas-linked-lists",
    "algoritmos-de-arboles/arboles-binarios": "arboles/arbol-binario",
    "algoritmos-de-arboles/recorridos-en-arboles-binarios": "arboles/arbol-binario",
    "implementacion-de-arboles/arboles-binarios-definicion-y-recorridos-preorden-inorden-postorden":
        "arboles/arbol-binario",
}


def _fix_nb_link(m):
    path = _NB_REMAP.get(m.group(1), m.group(1))
    return f'href="../{path}.html"'


def _first_page_url(node, page):
    """URL (relativa a `page`) de la primera página descendiente de una sección
    del nav: el destino natural de la 'sección' en las migas de pan. Para las
    secciones temáticas es su índice; para los subgrupos de notebooks, el primer
    notebook del grupo."""
    for child in getattr(node, "children", None) or []:
        if getattr(child, "is_page", False) and getattr(child, "url", None):
            if get_relative_url:
                return get_relative_url(child.url, page.url)
            return child.url
        if getattr(child, "is_section", False):
            u = _first_page_url(child, page)
            if u:
                return u
    return None


def _breadcrumb_html(page):
    """Migas de pan derivadas del nav (`page.ancestors`), iguales para páginas
    Markdown y notebooks: "📂 Sección › Subtema", enlazadas a su índice. Así, al
    aterrizar directo en una página (sobre todo un notebook titulado solo
    'Introducción'), se sabe a qué tema pertenece. Páginas de primer nivel
    (Inicio, Sobre mí) no llevan migas; tampoco se repite el título de la propia
    página (p. ej. en la portada de cada sección)."""
    anc = list(getattr(page, "ancestors", None) or [])      # cercano -> raíz
    titulos = [a for a in reversed(anc) if getattr(a, "title", None)]
    while titulos and titulos[-1].title == page.title:
        titulos.pop()
    if not titulos:
        return ""
    partes = []
    for sec in titulos:
        url = _first_page_url(sec, page)
        partes.append(f'<a href="{url}">{sec.title}</a>' if url else sec.title)
    return (
        '<p style="font-size:.78rem;color:var(--md-default-fg-color--light);'
        'margin:0 0 .5rem;">📂 ' + " › ".join(partes) + '</p>'
    )


def on_page_content(html, page, config, files):
    src = page.file.src_uri
    migas = _breadcrumb_html(page)
    if not src.endswith(".ipynb"):
        return migas + html
    # Corrige los enlaces internos heredados (ver nota en _NB_REMAP arriba).
    html = re.sub(r'href="\.\./notebook/([^"]+?)\.ipynb"', _fix_nb_link, html)
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
    return migas + boton + html
