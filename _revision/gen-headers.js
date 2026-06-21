#!/usr/bin/env node
// Genera ilustraciones por época (estilo según el contenido) → pages/assets/img/
const fs = require('fs')
const path = require('path')
const KEY = process.env.OPENAI_API_KEY
if (!KEY) { console.error('falta OPENAI_API_KEY'); process.exit(1) }
const OUT = path.join(__dirname, '..', 'pages', 'assets', 'img')
fs.mkdirSync(OUT, { recursive: true })

// Estética unificada: vaporwave + Blade Runner. La escena SIEMPRE figurativa y
// reconocible (personas, computadoras, robots, máquinas). El texto ya no importa.
const LOOK = 'Ilustración digital cinematográfica con estética vaporwave y Blade Runner: ciudad futurista oscura y lluviosa, neblina densa, luces de neón, rótulos luminosos, reflejos húmedos, atmósfera retro-futurista de ciencia ficción noir. Paleta de naranjas ámbar, magentas y cianes/teal sobre negros profundos, iluminación volumétrica y contraste cinematográfico.'

// [archivo-época, id, estilo, sujeto] — ~6 por época
const IMAGES = [
  // 1950s — retro
  ['1950', 'a', 'retro', 'La computadora ENIAC de los años 50 con tubos de vacío; primeras chispas de la inteligencia artificial.'],
  ['1950', 'b', 'retro', 'Una máquina traductora de 1954 con tarjetas perforadas convirtiendo palabras de un idioma a otro.'],
  ['1950', 'c', 'retro', 'El ingeniero Claude Shannon junto a diagramas de ondas de señales de comunicación.'],
  ['1950', 'd', 'retro', 'Retrato de Alan Turing observando pensativo una máquina computadora antigua.'],
  ['1950', 'e', 'retro', 'Un diagrama de árbol gramatical descomponiendo una oración en sus partes.'],
  ['1950', 'f', 'retro', 'Un científico de los años 50 frente a una consola de computadora gigante.'],
  // 1960s — isométrico
  ['1960', 'a', 'iso', 'Un espacio multidimensional de puntos proyectándose sobre un plano 2D (MDS).'],
  ['1960', 'b', 'iso', 'Un mapa donde palabras de significado parecido están cerca y las distintas lejos.'],
  ['1960', 'c', 'iso', 'Matemáticos trazando coordenadas de conceptos en una cuadrícula.'],
  ['1960', 'd', 'iso', 'Una forma compleja de muchas dimensiones aplanándose a dos dimensiones.'],
  ['1960', 'e', 'iso', 'Una constelación de puntos de datos formando grupos o clústeres.'],
  ['1960', 'f', 'iso', 'Distancias entre conceptos medidas con reglas en un espacio.'],
  // 1970s — iso/realista
  ['1970', 'a', 'iso', 'Una nube de datos reduciéndose a sus ejes principales, flechas de máxima varianza (PCA).'],
  ['1970', 'b', 'realista', 'Vectores de palabras emergiendo de una gran matriz de co-ocurrencia.'],
  ['1970', 'c', 'iso', 'Análisis estadístico del lenguaje con gráficos de dispersión coloridos.'],
  ['1970', 'd', 'realista', 'Semántica latente: significados ocultos bajo la superficie de las palabras.'],
  ['1970', 'e', 'iso', 'Autovectores como flechas dentro de una nube de datos elíptica.'],
  ['1970', 'f', 'realista', 'Patrones emergiendo de las frecuencias de palabras en un corpus.'],
  // 1980s — realista
  ['1980', 'a', 'realista', 'Una matriz términos-documentos descomponiéndose en tres bloques de luz (LSA / SVD).'],
  ['1980', 'b', 'realista', 'Una biblioteca digital donde la búsqueda encuentra documentos por su significado.'],
  ['1980', 'c', 'realista', 'Un haz de luz separando una gran matriz en sus componentes.'],
  ['1980', 'd', 'realista', 'Documentos y consultas encontrándose en un espacio de conceptos.'],
  ['1980', 'e', 'realista', 'Recuperación de información: los documentos relevantes brillando entre miles.'],
  ['1980', 'f', 'realista', 'Aproximación de rango reducido, conservando solo las señales más fuertes.'],
  // 1990s — sci-fi
  ['1990', 'a', 'scifi', 'Una red neuronal artificial brillante, nodos y conexiones iluminadas.'],
  ['1990', 'b', 'scifi', 'Una red neuronal recurrente procesando una secuencia de palabras en el tiempo.'],
  ['1990', 'c', 'scifi', 'Una señal apagándose capa tras capa: el gradiente que se desvanece.'],
  ['1990', 'd', 'scifi', 'Una red de Hopfield como memoria asociativa, patrones almacenados.'],
  ['1990', 'e', 'scifi', 'Representaciones distribuidas: el significado repartido entre muchas neuronas.'],
  ['1990', 'f', 'scifi', 'El renacimiento neuronal: cerebros y circuitos fusionándose.'],
  // 2000s — vibrante
  ['2000', 'a', 'vibrante', 'Documentos como mezclas de temas de colores (modelado de tópicos, LDA).'],
  ['2000', 'b', 'vibrante', 'Un corpus enorme de texto siendo analizado, big data del lenguaje.'],
  ['2000', 'c', 'vibrante', 'Distribuciones de probabilidad sobre palabras formando tópicos.'],
  ['2000', 'd', 'vibrante', 'Tópicos latentes emergiendo de un mar de documentos.'],
  ['2000', 'e', 'vibrante', 'Un símplex de Dirichlet colorido como triángulo de probabilidades.'],
  ['2000', 'f', 'vibrante', 'Artículos de noticias agrupándose en temas por color.'],
  // 2013 — vibrante
  ['2013', 'a', 'vibrante', 'El espacio vectorial de Word2Vec con la analogía rey - hombre + mujer = reina, flechas paralelas.'],
  ['2013', 'b', 'vibrante', 'Palabras transformándose en vectores densos de números.'],
  ['2013', 'c', 'vibrante', 'Una ventana de contexto deslizándose sobre una frase.'],
  ['2013', 'd', 'vibrante', 'Dos arquitecturas, CBOW y Skip-gram, como dos caminos espejados.'],
  ['2013', 'e', 'vibrante', 'Aritmética semántica: sumar y restar significados de palabras.'],
  ['2013', 'f', 'vibrante', 'Una galaxia de embeddings de palabras agrupados por significado.'],
  // 2017 — sci-fi
  ['2017', 'a', 'scifi', 'La arquitectura Transformer: atención conectando todas las palabras a la vez.'],
  ['2017', 'b', 'scifi', 'Self-attention: una palabra mirando simultáneamente a todas las demás.'],
  ['2017', 'c', 'scifi', 'Atención multi-cabeza: varios haces de atención en paralelo.'],
  ['2017', 'd', 'scifi', 'Codificación posicional: palabras con señales de su posición.'],
  ['2017', 'e', 'scifi', 'Los Transformers reemplazando a las redes recurrentes, lo viejo y lo nuevo.'],
  // 2018+ LLM — sci-fi
  ['2018', 'a', 'scifi', 'Un gran modelo de lenguaje gigantesco, miles de millones de parámetros brillando como una galaxia.'],
  ['2018', 'b', 'scifi', 'La evolución de BERT y GPT hacia ChatGPT, modelos creciendo en escala.'],
  ['2018', 'c', 'scifi', 'Una persona conversando con una IA en una interfaz de chat futurista.'],
  ['2018', 'd', 'scifi', 'RLHF: retroalimentación humana alineando a una inteligencia artificial.'],
  ['2018', 'e', 'scifi', 'IA multimodal: texto, imágenes y código fluyendo juntos.']
]

async function gen(im) {
  const [era, id, style, subject] = im
  const file = path.join(OUT, `${era}-${id}.png`)
  const t0 = Date.now()
  const prompt = `${LOOK}\n\nLa escena, FIGURATIVA y claramente reconocible (con personas, computadoras, robots o máquinas según corresponda), representa: "${subject}". Que se entienda a simple vista qué es, integrado de forma natural en ese mundo de ciencia ficción noir.`
  const res = await fetch('https://api.openai.com/v1/images/generations', {
    method: 'POST', headers: { 'Authorization': `Bearer ${KEY}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: 'gpt-image-1-mini', prompt, size: '1024x1024', quality: 'medium', n: 1 })
  })
  const j = await res.json()
  if (j.error) { console.log(`✗ ${era}-${id}: ${j.error.message}`); return }
  const b64 = j.data?.[0]?.b64_json
  if (!b64) { console.log(`✗ ${era}-${id}: sin imagen`); return }
  fs.writeFileSync(file, Buffer.from(b64, 'base64'))
  console.log(`✓ ${era}-${id} (${style}) ${((Date.now() - t0) / 1000).toFixed(0)}s`)
}

// 4 por época (ids a-d). En modo test, solo 3 representativas para aprobar el estilo.
const FOUR = IMAGES.filter((im) => 'abcd'.includes(im[1]))
const TEST = [
  ['1950', 'a', '', 'Un científico de los años 50 de pie frente a la enorme computadora ENIAC de tubos de vacío, ajustando cables; los primeros pasos de la inteligencia artificial.'],
  ['1990', 'a', '', 'Una ingeniera observando un robot pensante conectado a una gran red neuronal artificial de nodos luminosos flotando en el aire.'],
  ['2018', 'a', '', 'Una persona conversando cara a cara con un robot androide de inteligencia artificial frente a una pantalla holográfica gigante.']
]
const LIST = process.argv[2] === 'test' ? TEST : FOUR
;(async () => {
  for (const im of LIST) await gen(im)
  console.log(`\nListo. ${LIST.length} imágenes × $0.06 ≈ $${(LIST.length * 0.06).toFixed(2)}`)
})()
