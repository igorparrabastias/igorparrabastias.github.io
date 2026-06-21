# -*- coding: utf-8 -*-
"""Genera las páginas-índice por tema (python/estructuras/algoritmos/matematicas)
a partir del índice curado original apuntes-python.md, conservando el ORDEN y los
títulos, pero enlazando a los notebooks RENDERIZADOS en el sitio (no a GitHub).
Regenerable: si cambia el índice original, re-ejecutar."""
import re, os

SRC = "/home/nomikos/dev/tic-cursos-apuntes/pages/apuntes-python.md"
OUT = "/home/nomikos/dev/igorparrabastias.github.io/docs"

with open(SRC, encoding="utf-8") as fh:
    raw = fh.read()

# Partir en bloques por encabezado "## "
blocks = {}
cur = None
buf = []
for line in raw.splitlines():
    if line.startswith("## "):
        if cur is not None:
            blocks[cur] = "\n".join(buf).strip("\n")
        cur = line[3:].strip()
        buf = []
    else:
        buf.append(line)
if cur is not None:
    blocks[cur] = "\n".join(buf).strip("\n")

def find(sub):
    for k in blocks:
        if sub.lower() in k.lower():
            return k
    raise KeyError(sub)

def rewrite(body):
    # El índice original enlaza a GitHub (repo viejo). Lo reapuntamos a los notebooks
    # RENDERIZADOS en el sitio (las páginas están en docs/<tema>/, de ahí el ../).
    for pref in (
        "https://github.com/igorparrabastias/tic-cursos-apuntes/blob/master/notebook/",
        "https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/",
    ):
        body = body.replace(pref, "../notebook/")
    body = body.replace("(index-trees.md)", "(../index-trees.md)")
    return body

def section(sub, level="##"):
    k = find(sub)
    title = re.sub(r":[a-z_]+:\s*", "", k).strip()  # quita :bookmark_tabs:
    return f"{level} {title}\n\n{rewrite(blocks[k])}\n"

PAGES = {
 "python/index.md": {
   "h1": "Fundamentos de Python",
   "intro": (
     "El punto de partida del curso: de la sintaxis básica a la programación orientada a "
     "objetos y los rincones avanzados del lenguaje. Cada enlace abre el **notebook "
     "renderizado** en el sitio (y desde ahí, el botón *Abrir en Colab*).\n\n"
     "> [!TIP]\n"
     "> Si vienes empezando, ve en orden: el **Repaso básico** te da el piso firme antes "
     "de saltar a [Estructuras de datos](../estructuras/index.md) y "
     "[Algoritmos](../algoritmos/index.md). Si ya programas en Python, salta al avanzado.\n"),
   "secs": ["Python: Repaso Básico", "Python: Repaso Avanzado", "Anexos"],
   "tail": "",
 },
 "estructuras/index.md": {
   "h1": "Estructuras de datos",
   "intro": (
     "Cómo guardamos los datos para trabajar con ellos: nativas de Python, implementaciones "
     "propias y el mismo concepto en **otro lenguaje**. Cada enlace abre el notebook "
     "renderizado en el sitio.\n\n"
     "> [!TIP]\n"
     "> Elegir bien la estructura es la mitad de la solución; la otra mitad es el "
     "[algoritmo](../algoritmos/index.md) que la recorre. 🧩\n"),
   "secs": ["Estructuras de Datos Nativas de Python",
            "Implementación de Estructuras de Datos en Python",
            "Implementación de Estructuras Simples",
            "Árboles Y Algoritmos de Operaciones",
            "Implementación de Tablas Hash",
            "Implementación de Heaps"],
   "tail": (
     "## El mismo concepto, en JavaScript\n\n"
     "Las mismas estructuras (lista, pila, cola, grafo, hash, heap, BST) implementadas en "
     "JS con tests: **[Estructuras de datos en JavaScript](javascript.md)**.\n"),
 },
 "algoritmos/index.md": {
   "h1": "Algoritmos",
   "intro": (
     "Las recetas paso a paso: buscar, ordenar, recorrer grafos y encontrar caminos. Cada "
     "enlace abre el notebook renderizado en el sitio.\n\n"
     "> [!TIP]\n"
     "> Un algoritmo es una receta; la [estructura de datos](../estructuras/index.md) es la "
     "despensa. Sin buenos ingredientes ordenados, hasta la mejor receta tarda. ⏱️\n"),
   "secs": ["Algoritmos Básicos de Ordenamiento",
            "Algoritmos Básicos de Búsqueda",
            "Grafos 1: Algoritmos de Grafos",
            "Grafos 2: Recorrido de Grafos",
            "Grafos 3: Otras aplicaciones",
            "Implementación de Grafos"],
   "tail": (
     "## En JavaScript\n\n"
     "- **[Algoritmos en JavaScript](javascript.md)** — búsqueda, ordenamientos, Dijkstra, "
     "programación dinámica, recursión y backtracking.\n"
     "- **[Problemas resueltos en JavaScript](problemas-javascript.md)** — clásicos de "
     "entrevista con tests.\n"),
 },
 "matematicas/index.md": {
   "h1": "Matemáticas y teoría",
   "intro": (
     "La parte que separa al que *usa* algoritmos del que los *entiende*: complejidad, "
     "notación asintótica, recurrencias, computabilidad y cálculo. Cada enlace abre el "
     "notebook renderizado en el sitio.\n\n"
     "> [!TIP]\n"
     "> No necesitas ser matemático para programar bien, pero saber por qué un bucle "
     "anidado es O(n²) te ahorra noches de depuración. 🦉\n"),
   "secs": ["Técnicas de Análisis de Problemas",
            "Complejidad Algorítmica y Optimización",
            "Matemáticas y Teoría detrás de los Algoritmos"],
   "tail": (
     "## Cálculo\n\n"
     "- **[Cálculo 1A (MITx)](calculo-mitx.md)** — el lenguaje del cambio continuo, base "
     "de muchos métodos numéricos y de ML.\n"),
 },
}

for path, cfg in PAGES.items():
    parts = [f"# {cfg['h1']}\n", cfg["intro"], ""]
    for s in cfg["secs"]:
        parts.append(section(s))
    if cfg["tail"]:
        parts.append(cfg["tail"])
    out = os.path.join(OUT, path)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(parts).rstrip() + "\n")
    print("escrito:", path)
