#!/usr/bin/env node
// Genera ilustraciones para la sección "Para niños" → docs/assets/img/kids/
// Uso:  OPENAI_API_KEY=sk-... node _revision/gen-kids.js [test]
const fs = require('fs')
const path = require('path')
const KEY = process.env.OPENAI_API_KEY
if (!KEY) { console.error('falta OPENAI_API_KEY'); process.exit(1) }
const OUT = path.join(__dirname, '..', 'docs', 'assets', 'img', 'kids')
fs.mkdirSync(OUT, { recursive: true })

// Estética para peques: libro de cuentos, alegre y claro. SIN texto ni letras.
const LOOK = 'Ilustración estilo libro infantil para niños de 9 años: colores brillantes y alegres, formas redondeadas, personajes simpáticos y expresivos, trazo limpio, fondo simple, luz cálida y amable. Tierna y divertida, fácil de entender de un vistazo. SIN texto, SIN letras, SIN números escritos.'

// [archivo, sujeto]  — una imagen de portada por tema
const IMAGES = [
  ['ia', 'Un robot amistoso y sonriente aprendiendo mirando muchos libros y dibujos de colores; a su lado un loro listo que lo acompaña. La idea de una inteligencia que aprende de muchos ejemplos.'],
  ['python', 'Una niña feliz diciendo palabras mágicas a un computador sonriente que la obedece; una serpiente pitón simpática y de colores enroscada amistosamente cerca del teclado.'],
  ['estructuras', 'Cajas y cajones de colores para ordenar juguetes: una fila de vagones de tren, un cajón de calcetines y una pila de platos; todo ordenado y alegre.'],
  ['algoritmos', 'Niños felices armando una construcción de bloques tipo Lego siguiendo un manual de instrucciones paso a paso, con flechas que muestran el orden.'],
  ['matematicas', 'Un búho sabio y simpático con una lupa y una regla midiendo qué tan rápido baja un niño por un tobogán; números amistosos flotando alrededor.'],
  ['paradigmas', 'Varios niños construyendo lo mismo de maneras distintas: uno con bloques, otro siguiendo una receta, otro armando un rompecabezas; muchos estilos de jugar.'],
  ['practica', 'Niños entrenando y resolviendo retos en un gimnasio divertido de la programación, ganando medallas y estrellas doradas.'],
  ['redes', 'Varias computadoras y celulares simpáticos conectados con hilos de colores, enviándose cartitas y mensajes, como pasarse notas en la clase.'],
  ['web', 'Niños construyendo una página web como si fuera una casita de bloques de colores dentro de internet, pintando botones y dibujos.']
]

async function gen(im) {
  const [id, subject] = im
  const file = path.join(OUT, `${id}.png`)
  const t0 = Date.now()
  const prompt = `${LOOK}\n\nLa escena, FIGURATIVA y claramente reconocible, representa: "${subject}"`
  const res = await fetch('https://api.openai.com/v1/images/generations', {
    method: 'POST', headers: { 'Authorization': `Bearer ${KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'gpt-image-1-mini', prompt, size: '1024x1024', quality: 'medium', n: 1 })
  })
  const j = await res.json()
  if (j.error) { console.log(`✗ ${id}: ${j.error.message}`); return }
  const b64 = j.data?.[0]?.b64_json
  if (!b64) { console.log(`✗ ${id}: sin imagen`); return }
  fs.writeFileSync(file, Buffer.from(b64, 'base64'))
  console.log(`✓ ${id} ${((Date.now() - t0) / 1000).toFixed(0)}s`)
}

// En modo test solo genera 1 (ia) para aprobar el estilo antes de gastar en todas.
const LIST = process.argv[2] === 'test' ? IMAGES.slice(0, 1) : IMAGES
;(async () => {
  for (const im of LIST) await gen(im)
  console.log(`\nListo. ${LIST.length} imágenes × $0.06 ≈ $${(LIST.length * 0.06).toFixed(2)}`)
})()
