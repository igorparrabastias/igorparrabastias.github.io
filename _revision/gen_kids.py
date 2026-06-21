#!/usr/bin/env python3
"""Genera ilustraciones para la sección "Para kids" -> docs/assets/img/kids/
Usa la API de OpenAI Images (gpt-image-1-mini). Solo stdlib.

Uso:
  export $(cat ~/.config/igorparra-site/openai.env)   # carga OPENAI_API_KEY
  python3 _revision/gen_kids.py            # genera todas
  python3 _revision/gen_kids.py test       # solo 1 (ia), para aprobar el estilo
  python3 _revision/gen_kids.py ia python  # genera solo esas
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
OUT = os.path.join(REPO, "docs", "assets", "img", "kids")
os.makedirs(OUT, exist_ok=True)

LOOK = (
    "Ilustración estilo libro infantil para niños de 9 años: colores brillantes y "
    "alegres, formas redondeadas, personajes simpáticos y expresivos, trazo limpio, "
    "fondo simple, luz cálida y amable. Tierna y divertida, fácil de entender de un "
    "vistazo. SIN texto, SIN letras, SIN números escritos."
)

IMAGES = {
    "ia": "Un robot amistoso y sonriente aprendiendo mirando muchos libros y dibujos de colores; a su lado un loro listo que lo acompaña. La idea de una inteligencia que aprende de muchos ejemplos.",
    "python": "Una niña feliz diciendo palabras mágicas a un computador sonriente que la obedece; una serpiente pitón simpática y de colores enroscada amistosamente cerca del teclado.",
    "estructuras": "Cajas y cajones de colores para ordenar juguetes: una fila de vagones de tren, un cajón de calcetines y una pila de platos; todo ordenado y alegre.",
    "algoritmos": "Niños felices armando una construcción de bloques tipo Lego siguiendo un manual de instrucciones paso a paso, con flechas que muestran el orden.",
    "matematicas": "Un búho sabio y simpático con una lupa y una regla midiendo qué tan rápido baja un niño por un tobogán; números amistosos flotando alrededor.",
    "paradigmas": "Varios niños construyendo lo mismo de maneras distintas: uno con bloques, otro siguiendo una receta, otro armando un rompecabezas; muchos estilos de jugar.",
    "practica": "Niños entrenando y resolviendo retos en un gimnasio divertido de la programación, ganando medallas y estrellas doradas.",
    "redes": "Varias computadoras y celulares simpáticos conectados con hilos de colores, enviándose cartitas y mensajes, como pasarse notas en la clase.",
    "web": "Niños construyendo una página web como si fuera una casita de bloques de colores dentro de internet, pintando botones y dibujos.",
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
    path = os.path.join(OUT, f"{key_id}.png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64))
    print(f"✓ {key_id}  {time.time() - t0:.0f}s  -> {path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["test"]:
        keys = ["ia"]
    elif args:
        keys = [a for a in args if a in IMAGES]
    else:
        keys = list(IMAGES)
    for k in keys:
        gen(k, IMAGES[k])
    print(f"\nListo. {len(keys)} imágenes × $0.06 ≈ ${len(keys) * 0.06:.2f}")
