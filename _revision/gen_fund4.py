#!/usr/bin/env python3
"""Ilustraciones para la página 4 (Investigación reciente y futuro) -> docs/assets/img/
Estilo: 3D isométrico pulido, azul/cian neón, "fábrica tecnológica" futurista
(NO noir, NO Blade Runner). Usa OpenAI Images (gpt-image-1-mini). Solo stdlib.

Uso:
  export $(cat ~/.config/igorparra-site/openai.env)
  python3 _revision/gen_fund4.py test          # solo 1 (megacluster), aprobar estilo
  python3 _revision/gen_fund4.py razonamiento   # genera solo esa(s)
  python3 _revision/gen_fund4.py                # genera todas
"""
import base64
import json
import os
import sys
import time
import urllib.request

KEY = os.environ.get("OPENAI_API_KEY")
if not KEY:
    sys.exit("falta OPENAI_API_KEY")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO, "docs", "assets", "img")
os.makedirs(OUT, exist_ok=True)

LOOK = (
    "Ilustración 3D isométrica de alta calidad, render limpio y pulido estilo CGI. "
    "Estética de fábrica/tecnología futurista: superficies metálicas brillantes, vidrio, "
    "neón azul y cian luminoso, hologramas, líneas de luz, sobre fondo azul oscuro. "
    "Aspecto corporativo-sci-fi nítido y ordenado (NO noir, NO lluvia, NO Blade Runner, "
    "NO calle nocturna). Paleta dominante azul/cian/teal con acentos. "
    "SIN texto legible, SIN letras ni palabras escritas."
)

IMAGES = {
    "megacluster": "Un centro de datos colosal y futurista lleno de larguísimas filas de servidores y GPUs brillando con luz cian, una 'fábrica de inteligencia artificial', vista isométrica imponente.",
    "razonamiento": "Un cerebro de inteligencia artificial que despliega una larga cadena de pasos de pensamiento conectados y luminosos, uno tras otro, antes de llegar a una respuesta final brillante.",
    "rl": "Una inteligencia artificial central que recibe señales de recompensa y trofeos verificados desde flechas de retroalimentación que la rodean y la mejoran, idea de aprendizaje por refuerzo.",
    "moe": "Un enrutador central que dirige cada pequeño bloque de datos entrante hacia solo unos pocos módulos 'expertos' encendidos, mientras muchos otros módulos permanecen apagados (mezcla de expertos dispersa).",
    "contexto": "Una inteligencia artificial leyendo a la vez bibliotecas enteras y enormes bases de documentos, un gran flujo de páginas entrando hacia un foco de atención luminoso.",
    "ssm": "Un flujo continuo de datos avanzando linealmente por una tubería de cápsulas de estado que se van actualizando una tras otra, eficiente y ordenado (modelo de espacio de estados).",
    "energia_agua": "Un gran centro de datos futurista alimentado por torres de refrigeración con agua y por líneas de alta tensión eléctrica; corrientes de agua y de electricidad fluyendo hacia los servidores.",
    "espacio": "Satélites con grandes paneles solares y chips de computación orbitando el planeta Tierra, un centro de datos en el espacio iluminado por el Sol, vista desde la órbita.",
    "interpretabilidad": "Una lupa gigante examinando los circuitos y engranajes internos brillantes de un cerebro de inteligencia artificial, abriendo una caja negra para revelar sus mecanismos.",
    "conciencia": "Un robot humanoide pensativo contemplándose en un gran espejo, mirando su propio reflejo y preguntándose si hay alguien dentro; atmósfera serena y reflexiva.",
}

URL = "https://api.openai.com/v1/images/generations"


def gen(key_id, subject):
    prompt = f'{LOOK}\n\nLa escena, FIGURATIVA y claramente reconocible, representa: "{subject}"'
    body = json.dumps({
        "model": "gpt-image-1-mini",
        "prompt": prompt,
        "size": "1024x1024",
        "quality": "medium",
        "n": 1,
    }).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    })
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            j = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"✗ {key_id}: HTTP {e.code} {e.read().decode('utf-8', 'replace')[:200]}")
        return
    b64 = (j.get("data") or [{}])[0].get("b64_json")
    if not b64:
        print(f"✗ {key_id}: sin imagen")
        return
    path = os.path.join(OUT, f"f4-{key_id}.png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))
    print(f"✓ f4-{key_id}  {time.time() - t0:.0f}s  -> {path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["test"]:
        keys = ["megacluster"]
    elif args:
        keys = [a for a in args if a in IMAGES]
    else:
        keys = list(IMAGES)
    for k in keys:
        gen(k, IMAGES[k])
    print(f"\nListo. {len(keys)} imágenes × ~$0.06 ≈ ${len(keys) * 0.06:.2f}")
