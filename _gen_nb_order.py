"""Genera nb_order.py con el ORDEN pedagógico real, parseado de los índices
curados originales (apuntes-python.md e index-trees.md del repo tic-cursos-apuntes).
El orden = el de aparición de cada notebook en esos índices."""
import re, os, glob
from urllib.parse import unquote

SRCS = [
    "/home/nomikos/dev/tic-cursos-apuntes/pages/apuntes-python.md",
    "/home/nomikos/dev/tic-cursos-apuntes/pages/index-trees.md",
]
NB_DIR = "/home/nomikos/dev/igorparrabastias.github.io/notebook"

order = {}            # folder -> [stem, ...] en orden de aparición
for src in SRCS:
    with open(src, encoding="utf-8") as fh:
        txt = fh.read()
    for m in re.finditer(r'notebook/([^)\s"\']+?\.ipynb)', txt):
        rel = unquote(m.group(1))
        parts = rel.split("/")
        folder = parts[0]
        stem = os.path.splitext(parts[-1])[0]
        lst = order.setdefault(folder, [])
        if stem not in lst:
            lst.append(stem)

# Validación: comparar con los archivos reales en disco
real = {}
for p in glob.glob(os.path.join(NB_DIR, "**", "*.ipynb"), recursive=True):
    rel = os.path.relpath(p, NB_DIR)
    parts = rel.split(os.sep)
    folder = parts[0]
    real.setdefault(folder, set()).add(os.path.splitext(parts[-1])[0])

print("=== VALIDACIÓN ===")
for folder in sorted(set(list(order) + list(real))):
    listados = order.get(folder, [])
    en_disco = real.get(folder, set())
    faltan_en_disco = [s for s in listados if s not in en_disco]   # listado pero no existe
    sin_listar = sorted(en_disco - set(listados))                  # existe pero no listado
    print(f"\n[{folder}] listados={len(listados)} en_disco={len(en_disco)}")
    if faltan_en_disco:
        print(f"  ⚠ listados pero NO en disco: {faltan_en_disco}")
    if sin_listar:
        print(f"  + sin listar (irán al final): {sin_listar}")

# Emitir nb_order.py
with open("/home/nomikos/dev/igorparrabastias.github.io/nb_order.py", "w", encoding="utf-8") as out:
    out.write("# -*- coding: utf-8 -*-\n")
    out.write('"""Orden pedagógico de los notebooks por carpeta (generado por _gen_nb_order.py\n')
    out.write("desde los índices curados originales). NO editar a mano: regenerar.\"\"\"\n")
    out.write("ORDER = {\n")
    for folder in sorted(order):
        out.write(f"    {folder!r}: [\n")
        for stem in order[folder]:
            out.write(f"        {stem!r},\n")
        out.write("    ],\n")
    out.write("}\n")
print("\n=> nb_order.py escrito con", len(order), "carpetas")
