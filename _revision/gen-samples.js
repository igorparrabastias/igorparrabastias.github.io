#!/usr/bin/env node
// Genera 1 imagen de prueba por cada opción (mismo prompt) para comparar calidad/costo.
// Usa OPENAI_API_KEY del entorno. Guarda PNGs en pages/assets/samples/.
const fs = require('fs')
const path = require('path')

const KEY = process.env.OPENAI_API_KEY
if (!KEY) { console.error('falta OPENAI_API_KEY'); process.exit(1) }

const OUT = path.join(__dirname, '..', 'pages', 'assets', 'samples')
fs.mkdirSync(OUT, { recursive: true })

const PROMPT = `Ilustración editorial elegante para el capítulo de un libro sobre la historia de la inteligencia artificial, titulado "Década de 1950: fundamentos del análisis semántico". Una computadora gigante de los años 1950 con tubos de vacío y tarjetas perforadas; de ella salen líneas de luz que fluyen hacia palabras flotantes que se transforman en vectores geométricos y puntos en un espacio. Estilo arte de línea limpio y minimalista, paleta índigo (#3a47b8) con acentos cálidos sobre fondo color crema claro. Elegante, sin texto, sin letras.`

const CONFIGS = [
  { id: 'gpt-image-2-high',   model: 'gpt-image-2',      quality: 'high',   cost: 0.120 },
  { id: 'gpt-image-2-medium', model: 'gpt-image-2',      quality: 'medium', cost: 0.060 },
  { id: 'gpt-image-2-low',    model: 'gpt-image-2',      quality: 'low',    cost: 0.030 },
  { id: 'mini-medium',        model: 'gpt-image-1-mini', quality: 'medium', cost: 0.016 }
]

async function gen(cfg) {
  const t0 = Date.now()
  const res = await fetch('https://api.openai.com/v1/images/generations', {
    method: 'POST',
    headers: { 'Authorization': `Bearer ${KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: cfg.model, prompt: PROMPT, size: '1024x1024', quality: cfg.quality, n: 1 })
  })
  const j = await res.json()
  if (j.error) { console.log(`✗ ${cfg.id}: ${j.error.message}`); return null }
  const b64 = j.data?.[0]?.b64_json
  if (!b64) { console.log(`✗ ${cfg.id}: sin imagen`); return null }
  const file = path.join(OUT, `${cfg.id}.png`)
  fs.writeFileSync(file, Buffer.from(b64, 'base64'))
  const secs = ((Date.now() - t0) / 1000).toFixed(0)
  console.log(`✓ ${cfg.id.padEnd(18)} $${cfg.cost.toFixed(3)}  ${secs}s  → ${file}`)
  return { ...cfg, file }
}

;(async () => {
  const results = []
  for (const c of CONFIGS) results.push(await gen(c))
  const ok = results.filter(Boolean)
  console.log(`\n${ok.length}/${CONFIGS.length} generadas. Costo total ≈ $${ok.reduce((s, r) => s + r.cost, 0).toFixed(3)}`)
})()
