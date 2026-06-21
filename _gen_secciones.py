"""Reestructura los índices temáticos "por sección": dentro de cada ## sección que
tenga jerarquía (ítems con sub-ítems), cada notebook de primer nivel pasa a ser un
subtítulo ### (enlace clicable) y sus ejercicios quedan como viñetas debajo. Las
secciones que ya son listas planas (sin sub-ítems) se dejan igual.

Uso:  python3 _gen_secciones.py [--apply] docs/algoritmos/index.md ...
Sin --apply solo imprime el resultado (preview)."""
import re
import sys

TOP = re.compile(r'^- (.*)$')
CHILD = re.compile(r'^  - (.*)$')
EMOJI = re.compile(r'^(:[a-z0-9_+\-]+:\s*)?(.*)$')


def split_sections(lines):
    """Devuelve [(cabecera_o_None, [líneas])] partiendo en cada '## '."""
    secs, cur, head = [], [], None
    for ln in lines:
        if ln.startswith('## '):
            secs.append((head, cur)); head, cur = ln, []
        else:
            cur.append(ln)
    secs.append((head, cur))
    return secs


def sectionize(body):
    if not any(CHILD.match(l) for l in body):
        return body                      # lista plana: no se toca
    out = []
    for l in body:
        mc = CHILD.match(l)
        mt = TOP.match(l)
        if mc:                           # ejercicio -> viñeta de primer nivel
            out.append('- ' + mc.group(1).rstrip())
        elif mt:                         # notebook -> subtítulo ###
            txt = EMOJI.match(mt.group(1)).group(2).rstrip()
            if out and out[-1].strip():
                out.append('')
            out.append('### ' + txt)
            out.append('')
        else:
            out.append(l.rstrip())
    # colapsa 3+ líneas en blanco a 1
    res = []
    for l in out:
        if l == '' and res and res[-1] == '':
            continue
        res.append(l)
    return res


def transform(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    out = []
    for head, body in split_sections(lines):
        if head is not None:
            out.append(head)
        out.extend(sectionize(body))
    txt = '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', txt).rstrip() + '\n'


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    files = [a for a in sys.argv[1:] if a != '--apply']
    for f in files:
        res = transform(f)
        if apply:
            open(f, 'w', encoding='utf-8').write(res)
            print('escrito:', f)
        else:
            print('=== PREVIEW', f, '===')
            print(res)
