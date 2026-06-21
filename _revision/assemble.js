#!/usr/bin/env node
// Ensambla las secciones (out/*.md) en una SERIE de páginas:
//   - landing (intro + línea de tiempo + enlaces a las 4 partes)
//   - 4 páginas temáticas, cada una con iconos por nivel, chistes (callouts),
//     figuras (imágenes IA + diagramas SVG) e índice propio con anclas que
//     funcionan en MkDocs.
const fs = require('fs')
const path = require('path')

const OUT = path.join(__dirname, 'out')
const PAGES_DIR = path.join(__dirname, '..', 'pages')

const ICON = { 2: '🏠', 3: '👾', 4: '📌' }
const C = (s) => '> [!TIP] 😄 Pausa\n' + s.split('\n').map((l) => '> ' + l).join('\n')
const imgB = (file, alt, w = 460) => `<p align="center"><img src="assets/${file}" alt="${alt}" width="${w}"></p>`

// --- Definición de la serie -------------------------------------------------
const LANDING = 'fundamento-del-pln-y-la-ia.md'
const PARTS = [
  { file: 'fundamentos-1-origenes.md', n: 1,
    title: 'Orígenes del PLN y la IA (1950–1979)',
    sections: ['01-1950s.md', '02-1960s.md', '03-1970s.md'] },
  { file: 'fundamentos-2-estadistica-redes.md', n: 2,
    title: 'Estadística y redes neuronales (1980–2000s)',
    sections: ['04-1980s.md', '05-1990s.md', '06-2000s.md'] },
  { file: 'fundamentos-3-era-llm.md', n: 3,
    title: 'La era de los grandes modelos de lenguaje (2013–2026)',
    sections: ['07-2013-word2vec.md', '08-2017-llm.md', '09-como-funcionan-llm-hoy.md',
      '10-agentes.md', '11-infraestructura-chips.md', '12-multimodalidad-evaluacion.md'] },
  { file: 'fundamentos-4-investigacion-futuro.md', n: 4,
    title: 'Investigación reciente y futuro próximo',
    sections: ['13-investigacion-futuro.md'] }
]
const NAVNAMES = ['Intro', '1 · Orígenes', '2 · Estadística y redes', '3 · Era LLM', '4 · Investigación y futuro']
const NAVFILES = [LANDING, ...PARTS.map((p) => p.file)]

// --- Chistes por sección (MID tras el 1er ###, END al final) ----------------
const MID = {
  '01-1950s.md': C('Shannon midió la información en bits. Tu grupo de WhatsApp familiar transmite millones de bits y cero información.'),
  '02-1960s.md': C('Reducir dimensiones suena fácil hasta que intentas explicar tu semana en un solo número.'),
  '03-1970s.md': C('Un autovector es el que no cambia de dirección cuando lo transformas. Como ese amigo que opina lo mismo pase lo que pase.'),
  '04-1980s.md': C('SVD parte una matriz en tres. Es básicamente un divorcio de matrices, pero todos quedan en buenos términos.'),
  '05-1990s.md': C('Backpropagation: aprender de los errores propagándolos hacia atrás. Algo que los humanos llevamos haciendo mal desde siempre.'),
  '06-2000s.md': C('Un "tópico" en LDA es una distribución de palabras. Mi tópico favorito es una distribución de siestas.'),
  '07-2013-word2vec.md': C('Word2Vec aprende del contexto: "dime con qué palabras andas y te diré qué significas".'),
  '09-como-funcionan-llm-hoy.md': C('Un LLM no lee letras, lee "tokens" (trozos de palabra). Por eso a veces cuenta mal las erres de "ferrocarril": ve pedazos, no letras. Tú tampoco cuentas bien sin los dedos, no juzgues.'),
  '10-agentes.md': C('Un agente planifica, usa herramientas y se autocorrige. Como tú en un lunes productivo, pero sin café y sin crisis existencial.'),
  '11-infraestructura-chips.md': C('Una GPU hace millones de multiplicaciones en paralelo. Tu cerebro hace una resta y ya pide vacaciones.'),
  '12-multimodalidad-evaluacion.md': C('Multimodal significa que entiende texto, imágenes y audio a la vez. Como tú viendo una serie mientras chateas y escuchas música: caótico, pero funciona.'),
  '13-investigacion-futuro.md': C('Los modelos de razonamiento "piensan más antes de responder". Una virtud que seguimos sin lograr enseñarle a internet.')
}
const END = {
  '01-1950s.md': C('En 1950, Turing preguntó si las máquinas podían pensar. 75 años después, siguen sin poder estacionar.'),
  '02-1960s.md': C('El MDS reduce mil dimensiones a dos. Mi capacidad de atención hizo lo mismo con este párrafo.'),
  '03-1970s.md': C('El PCA apunta a la dirección de máxima varianza. Como tu tío en Navidad: siempre hacia donde hay más drama.'),
  '04-1980s.md': C('LSA descompone el significado en valores singulares. Yo me descompongo en cualquier reunión antes de las 9 am.'),
  '05-1990s.md': C('Las redes de los 90 sufrían el *vanishing gradient*: la motivación se desvanece capa tras capa. Relatable.'),
  '06-2000s.md': C('LDA asume que cada documento es una mezcla de tópicos. Este: 60% historia, 30% álgebra, 10% chistes malos.'),
  '07-2013-word2vec.md': C('Restas "hombre" a "rey" y sumas "mujer" → "reina". Restas el café a un lunes → nada bueno.'),
  '08-2017-llm.md': C('De Word2Vec a ChatGPT en una década. Y todavía le ponemos "por favor" por si acaso.'),
  '09-como-funcionan-llm-hoy.md': C('Entrenar un modelo es predecir la siguiente palabra millones de veces. Básicamente, autocompletar con esteroides y un doctorado.'),
  '10-agentes.md': C('Le damos a la IA acceso a herramientas para que actúe sola. "¿Qué podría salir mal?", dijo la humanidad, optimista.'),
  '11-infraestructura-chips.md': C('Entrenar un modelo grande consume la electricidad de un pueblo entero. La inteligencia artificial es brillante; la factura, también.'),
  '12-multimodalidad-evaluacion.md': C('Evaluamos modelos con exámenes que ellos mismos acaban estudiando. Es como dejar el examen sobre la mesa y luego fingir sorpresa por las notas.')
}

// --- Imágenes y diagramas por sección ---------------------------------------
const photos = (era, ids) => ids.map((id) => imgB(`img/${era}-${id}.png`, 'Ilustración'))
const MEDIA = {
  '01-1950s.md': { header: imgB('img/1950-a.png', 'Ilustración'), inline: photos('1950', ['b', 'c', 'd']) },
  '02-1960s.md': { header: imgB('img/1960-a.png', 'Ilustración'), inline: photos('1960', ['b', 'c', 'd']) },
  '03-1970s.md': { header: imgB('img/1970-a.png', 'Ilustración'), inline: photos('1970', ['b', 'c', 'd']) },
  '04-1980s.md': { header: imgB('img/1980-a.png', 'Ilustración'), inline: [imgB('svd.svg', 'SVD: A ≈ U·Σ·Vᵀ', 520), ...photos('1980', ['b', 'c', 'd'])] },
  '05-1990s.md': { header: imgB('img/1990-a.png', 'Ilustración'), inline: photos('1990', ['b', 'c', 'd']) },
  '06-2000s.md': { header: imgB('img/2000-a.png', 'Ilustración'), inline: photos('2000', ['b', 'c', 'd']) },
  '07-2013-word2vec.md': { header: imgB('img/2013-a.png', 'Ilustración'), inline: [imgB('word2vec.svg', 'rey − hombre + mujer ≈ reina', 420), ...photos('2013', ['b', 'c', 'd'])] },
  '08-2017-llm.md': { header: imgB('img/2017-a.png', 'Ilustración'), inline: [imgB('attention.svg', 'Atención Q/K/V', 580), ...photos('2017', ['b', 'c', 'd']), ...photos('2018', ['a', 'b', 'c', 'd'])] }
}

// --- Utilidades -------------------------------------------------------------
function injectAfter(text, re, block) {
  if (!block) return text
  const lines = text.split('\n')
  const i = lines.findIndex((l) => re.test(l))
  if (i === -1) return text + '\n\n' + block
  lines.splice(i + 1, 0, '', block, '')
  return lines.join('\n')
}

// Header tras el ##; imágenes inline repartidas entre los ### (saltando el 1º, que lleva el chiste).
function injectMedia(text, media) {
  if (!media) return text
  let lines = injectAfter(text, /^## /, media.header).split('\n')
  const h3 = []
  lines.forEach((l, i) => { if (/^### /.test(l)) h3.push(i) })
  const inl = media.inline || []
  if (inl.length && h3.length > 1) {
    const step = Math.max(1, Math.floor(h3.length / (inl.length + 1)))
    const placed = inl.map((blk, k) => [h3[Math.min(h3.length - 1, (k + 1) * step)], blk])
    placed.sort((a, b) => b[0] - a[0]).forEach(([pos, blk]) => lines.splice(pos + 1, 0, '', blk, ''))
  }
  return lines.join('\n')
}

function read(f) {
  const p = path.join(OUT, f)
  if (!fs.existsSync(p)) { console.error('FALTA sección:', f); process.exit(1) }
  return fs.readFileSync(p, 'utf8').trim()
}

// Anclas IGUALES a las que genera MkDocs Material (emoji → guion inicial; duplicados con _N).
function makeSlugger() {
  const seen = {}
  return function slug(text) {
    let s = text.toLowerCase()
      .replace(/[^\w\sÀ-ɏ-]/gu, '')
      .replace(/\s+/g, '-')
      .replace(/-+$/g, '')
    if (seen[s] === undefined) { seen[s] = 0; return s }
    seen[s] += 1; return `${s}_${seen[s]}`
  }
}

function addIcons(body) {
  return body.split('\n').map((line) => {
    const m = line.match(/^(#{2,4}) (.+)$/)
    return m ? `${m[1]} ${ICON[m[1].length]} ${m[2]}` : line
  }).join('\n')
}

function buildTOC(body) {
  const slug = makeSlugger()
  const toc = []
  for (const line of body.split('\n')) {
    const m = line.match(/^(#{2,3}) (.*)$/)
    if (!m) continue
    const text = m[2].replace(/\s+#*$/, '').trim()
    if (/Índice$/i.test(text)) continue
    toc.push(`${m[1].length === 2 ? '' : '    '}- [${text}](#${slug(text)})`)
  }
  return `## 📑 Índice\n\n${toc.join('\n')}`
}

function seriesNav(activeIdx) {
  return '**Serie _Fundamentos del PLN y la IA_:** ' + NAVNAMES.map((name, i) =>
    i === activeIdx ? `**${name}**` : `[${name}](${NAVFILES[i]})`).join(' · ')
}

// --- Landing ----------------------------------------------------------------
function buildLanding() {
  let txt = read('00-front.md')
  const contenido = `## 📚 La serie, en 4 partes

Este recorrido está dividido en cuatro páginas; puedes leerlas en orden:

1. **[Orígenes (1950–1979)](${PARTS[0].file})** — bases lingüísticas y matemáticas del significado: MDS, PCA y semántica latente.
2. **[Estadística y redes neuronales (1980–2000s)](${PARTS[1].file})** — LSA/SVD, el renacer de las redes neuronales y el *topic modeling* (LDA).
3. **[La era de los LLM (2013–2026)](${PARTS[2].file})** — de Word2Vec y los Transformers a cómo funcionan los LLM hoy: agentes, infraestructura y multimodalidad.
4. **[Investigación reciente y futuro próximo](${PARTS[3].file})** — modelos de razonamiento, MoE, el debate sobre la AGI y los retos abiertos.`
  txt = txt.replace('<!--TOC-->', contenido)
  fs.writeFileSync(path.join(PAGES_DIR, LANDING), txt + '\n')
  return txt
}

// --- Páginas de la serie ----------------------------------------------------
function buildPart(part, idx) {
  const parts = []
  part.sections.forEach((f) => {
    let txt = read(f)
    if (f === '08-2017-llm.md') txt = txt.split(/^## Conclusión General/m)[0].trim() // la conclusión global va en la pág. 4
    txt = injectMedia(txt, MEDIA[f])
    txt = injectAfter(txt, /^### /, MID[f])
    if (END[f]) txt += '\n\n' + END[f]
    parts.push(txt)
  })
  let body = addIcons(parts.join('\n\n'))
  const toc = buildTOC(body)
  const page = [
    `# ${part.n} · ${part.title}`,
    seriesNav(idx + 1),
    toc,
    '---',
    body
  ].join('\n\n')
  fs.writeFileSync(path.join(PAGES_DIR, part.file), page + '\n')
  return page
}

// --- Run --------------------------------------------------------------------
buildLanding()
let totalW = 0, totalImg = 0, totalJokes = 0
PARTS.forEach((p, i) => {
  const page = buildPart(p, i)
  const w = page.split(/\s+/).filter(Boolean).length
  const img = (page.match(/<img /g) || []).length
  const jokes = (page.match(/\[!TIP\]/g) || []).length
  totalW += w; totalImg += img; totalJokes += jokes
  console.log(`${p.file.padEnd(40)} ${String(w).padStart(5)} pal · ${img} img · ${jokes} chistes`)
})
console.log(`\nTOTAL serie: ${totalW} palabras · ${totalImg} imágenes · ${totalJokes} chistes · ~${Math.round(totalW / 450)} págs`)
console.log(`Landing: ${LANDING}`)
