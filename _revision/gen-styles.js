#!/usr/bin/env node
// Muestrario de ESTILOS (mismo tema, a color) con gpt-image-1-mini. → pages/assets/styles/
const fs = require('fs')
const path = require('path')
const KEY = process.env.OPENAI_API_KEY
if (!KEY) { console.error('falta OPENAI_API_KEY'); process.exit(1) }
const OUT = path.join(__dirname, '..', 'pages', 'assets', 'styles')
fs.mkdirSync(OUT, { recursive: true })

// Tema constante; varía solo el ESTILO. Insistimos en "sin texto" (la Mini tiende a meter letras).
const SUBJECT = 'Una computadora gigante de los años 1950 con tarjetas perforadas, de la que emanan palabras que se transforman en vectores y puntos conectados en un espacio. Tema: la historia de la inteligencia artificial y el lenguaje.'
const NOTEXT = 'ABSOLUTAMENTE sin texto, sin palabras, sin letras, sin números, sin tipografía de ningún tipo.'

const STYLES = [
  { id: '1-retro-color',  desc: 'Retro a color (póster vintage 50s-60s)', style: 'Estilo de póster retro vintage de los años 50-60, colores vivos y cálidos (mostaza, turquesa, rojo coral, naranja, crema), formas planas, arte de línea grueso.' },
  { id: '2-realista',     desc: 'Realista / 3D cinematográfico', style: 'Render fotorrealista 3D con iluminación cinematográfica, materiales detallados, profundidad de campo, colores ricos y realistas.' },
  { id: '3-scifi-neon',   desc: 'Sci-fi futurista / neón cyberpunk', style: 'Ciencia ficción futurista con estética cyberpunk: luces de neón azul, magenta y cian, brillos, reflejos, atmósfera oscura y dramática de alta tecnología.' },
  { id: '4-vibrante',     desc: 'Ilustración vibrante moderna', style: 'Ilustración digital moderna y vibrante, colores saturados y alegres, degradados suaves, estilo editorial tecnológico actual.' },
  { id: '5-isometrico',   desc: 'Isométrico 3D (infografía)', style: 'Ilustración isométrica 3D limpia, paleta pastel variada y colorida, estilo de infografía moderna, sombras suaves.' },
  { id: '6-acuarela',     desc: 'Acuarela artística', style: 'Pintura en acuarela artística, colores suaves y fluidos que se mezclan, pinceladas expresivas, papel texturizado.' }
]

async function gen(s) {
  const t0 = Date.now()
  const prompt = `${SUBJECT}\n\nEstilo visual: ${s.style}\n\n${NOTEXT}`
  const res = await fetch('https://api.openai.com/v1/images/generations', {
    method: 'POST', headers: { 'Authorization': `Bearer ${KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'gpt-image-1-mini', prompt, size: '1024x1024', quality: 'medium', n: 1 })
  })
  const j = await res.json()
  if (j.error) { console.log(`✗ ${s.id}: ${j.error.message}`); return }
  const b64 = j.data?.[0]?.b64_json
  if (!b64) { console.log(`✗ ${s.id}: sin imagen`); return }
  fs.writeFileSync(path.join(OUT, `${s.id}.png`), Buffer.from(b64, 'base64'))
  console.log(`✓ ${s.id.padEnd(16)} ${((Date.now() - t0) / 1000).toFixed(0)}s  ${s.desc}`)
}

;(async () => {
  for (const s of STYLES) await gen(s)
  console.log(`\nListo. ${STYLES.length} estilos × $0.016 ≈ $${(STYLES.length * 0.016).toFixed(3)}`)
})()
