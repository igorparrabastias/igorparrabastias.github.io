# 2 · Estadística y redes neuronales (1980–2000s)

**Serie _Fundamentos del PLN y la IA_:** [Intro](fundamento-del-pln-y-la-ia.md) · [1 · Orígenes](fundamentos-1-origenes.md) · **2 · Estadística y redes** · [3 · Era LLM](fundamentos-3-era-llm.md) · [4 · Investigación y futuro](fundamentos-4-investigacion-futuro.md)

## 📑 Índice

- [🏠 Década de 1980: Latent Semantic Analysis (LSA)](#-década-de-1980-latent-semantic-analysis-lsa)
    - [👾 Desarrollo de LSA para representar y analizar grandes volúmenes de texto](#-desarrollo-de-lsa-para-representar-y-analizar-grandes-volúmenes-de-texto)
    - [👾 Fundamentos del LSA](#-fundamentos-del-lsa)
    - [👾 Proceso de LSA](#-proceso-de-lsa)
    - [👾 El impacto de esta técnica en la comprensión automática del lenguaje](#-el-impacto-de-esta-técnica-en-la-comprensión-automática-del-lenguaje)
    - [👾 Conclusión](#-conclusión)
- [🏠 Década de 1990: Redes Neuronales y Representaciones Distribuidas](#-década-de-1990-redes-neuronales-y-representaciones-distribuidas)
    - [👾 Uso Temprano de Redes Neuronales para Representaciones Distribuidas](#-uso-temprano-de-redes-neuronales-para-representaciones-distribuidas)
    - [👾 Avances y Limitaciones frente a Enfoques Posteriores](#-avances-y-limitaciones-frente-a-enfoques-posteriores)
    - [👾 Conclusión](#-conclusión_1)
- [🏠 Primeros 2000: Modelos Probabilísticos y Topic Modeling](#-primeros-2000-modelos-probabilísticos-y-topic-modeling)
    - [👾 Introducción de Modelos como Latent Dirichlet Allocation (LDA)](#-introducción-de-modelos-como-latent-dirichlet-allocation-lda)
    - [👾 Cómo los Modelos Probabilísticos Influyeron en la Semántica Vectorial](#-cómo-los-modelos-probabilísticos-influyeron-en-la-semántica-vectorial)
    - [👾 Conclusión](#-conclusión_2)

---

## 🏠 Década de 1980: Latent Semantic Analysis (LSA)

<p align="center"><img src="assets/img/1980-a.png" alt="Ilustración" width="460"></p>


### 👾 Desarrollo de LSA para representar y analizar grandes volúmenes de texto

> [!TIP] 😄 Pausa
> SVD parte una matriz en tres. Es básicamente un divorcio de matrices, pero todos quedan en buenos términos.


#### 📌 Orígenes del LSA

El Análisis Semántico Latente (LSA, por sus siglas en inglés) fue propuesto formalmente por Deerwester et al. en 1990, aunque su desarrollo y las ideas que lo sustentan comenzaron a surgir durante la década de 1980. Este método se convirtió en un hito del procesamiento del lenguaje natural (PLN) y la recuperación de información gracias a su capacidad de capturar relaciones semánticas entre términos y documentos, superando las limitaciones de las búsquedas tradicionales basadas en palabras clave.

Antes de LSA, los sistemas de búsqueda dependían de la coincidencia exacta de palabras clave. Si un usuario buscaba un término específico, el sistema solo recuperaba documentos que contuvieran exactamente ese término, lo que resultaba ineficaz ante sinónimos o polisemia. El objetivo principal de LSA era abordar este problema representando palabras y documentos en un espacio semántico compartido, donde las similitudes entre términos se basaran en contextos y no solo en coincidencias literales.

#### 📌 Limitaciones de las búsquedas basadas en palabras clave

Las búsquedas por palabras clave fueron durante mucho tiempo el método estándar para recuperar información, pero presentan varias limitaciones inherentes que afectan la precisión y relevancia de los resultados:

1. **Ambigüedad lingüística**: una palabra puede tener varios significados según el contexto. "Banco" puede referirse a una entidad financiera o a un objeto para sentarse; sin un contexto claro, el motor de búsqueda puede devolver resultados irrelevantes.
2. **Sinónimos y variaciones léxicas**: este enfoque no considera la diversidad del lenguaje. Una búsqueda de "automóvil" no devuelve documentos que contengan "coche" o "vehículo", lo que limita encontrar información relevante.
3. **Falta de comprensión semántica**: no se entiende el significado detrás de las palabras. La consulta "mejores restaurantes italianos" puede no captar que el usuario busca recomendaciones, no solo una lista de nombres.
4. **Dependencia del formato de consulta**: los usuarios no siempre formulan la consulta de forma óptima, y la manera de estructurarla condiciona los resultados aunque la idea de búsqueda sea clara.

#### 📌 Enfoques para superar las limitaciones

Para abordar estas limitaciones se han desarrollado enfoques que permiten una representación semántica más rica y una comprensión más profunda del lenguaje natural:

- **Modelos de lenguaje basados en contexto**: con el avance del aprendizaje profundo, modelos como BERT (Bidirectional Encoder Representations from Transformers) y GPT (Generative Pre-trained Transformer) revolucionaron el procesamiento de las consultas. Captan el contexto de las palabras en una oración para desambiguar significados y generan representaciones semánticas que reflejan la intención del usuario, mejorando la relevancia de los resultados.
- **Análisis de sentimientos y entidades**: identificar entidades y analizar sentimientos permite comprender mejor lo que busca el usuario; por ejemplo, reconocer que "mejores" en "mejores restaurantes italianos" implica una evaluación cualitativa.
- **Búsqueda semántica**: parte de que los sistemas deben entender el significado y no solo la forma. Se apoya en **ontologías** (representaciones estructuradas de conocimiento que definen las relaciones entre conceptos) y en **grafos de conocimiento** (estructuras que almacenan entidades y sus relaciones, facilitando la recuperación basada en significado).
- **Interacción natural con el usuario**: interfaces que permiten consultas en lenguaje natural, como los asistentes virtuales, capaces de interpretar preguntas complejas y devolver respuestas más precisas y relevantes.

La evolución hacia métodos que incorporan una comprensión semántica más profunda, considerando el contexto, las relaciones semánticas y la intención del usuario, transforma la manera en que interactuamos con la información.

### 👾 Fundamentos del LSA

<p align="center"><img src="assets/svd.svg" alt="SVD: A ≈ U·Σ·Vᵀ" width="520"></p>


#### 📌 Descomposición en Valores Singulares (SVD)

La Descomposición en Valores Singulares (SVD) es una técnica crucial del álgebra lineal que descompone una matriz en tres matrices componentes. Es una herramienta fundamental en aplicaciones como el procesamiento de señales, la compresión de imágenes y, de manera muy relevante, en el PLN y la reducción de dimensionalidad para el análisis de grandes volúmenes de datos.

**Definición formal.** Dada una matriz A de dimensión m×n, la SVD la expresa como el producto de tres matrices:

```
A  =  U · Σ · Vᵀ          (A: m×n)

U   ortogonal m×m  → columnas = vectores singulares izquierdos
                     (direcciones de las filas originales de A)
Σ   diagonal m×n   → valores singulares ≥ 0, ordenados de mayor a menor
Vᵀ  transpuesta de V ortogonal n×n
                     columnas de V = vectores singulares derechos
                     (direcciones de las columnas originales de A)
```

Los valores de la diagonal Σ se denominan **valores singulares** y representan la magnitud de las dimensiones más importantes de la matriz original: indican qué tan significativa es cada dimensión en la representación de los datos.

**Aplicaciones en reducción de dimensionalidad.** La SVD simplifica datos complejos de alta dimensionalidad. Al eliminar las dimensiones con valores singulares pequeños se retienen las características más importantes, reduciendo el ruido y manteniendo la esencia de la información:

- **PLN**: la SVD es central en técnicas como LSA, donde descompone una matriz término-documento. Esto ayuda a identificar temas subyacentes en un corpus grande y a representar documentos y términos en un espacio de menor dimensión.
- **Compresión de datos**: en la compresión de imágenes, permite representar una imagen con un menor número de dimensiones sin perder demasiada calidad visual, reconstruyéndola con los valores singulares más significativos.
- **Filtrado de ruido**: al reducir las dimensiones se eliminan las componentes que corresponden a ruido o información redundante, mejorando la calidad de los datos procesados.

**Ventajas**: reduce la dimensionalidad (datos más manejables, algoritmos más rápidos y con menos memoria), mejora la interpretación de las principales características o patrones y aporta robustez frente al ruido.

**Limitaciones**: la descomposición es computacionalmente costosa, sobre todo en matrices grandes; y si se agregan nuevos datos a la matriz original, la SVD debe recalcularse desde cero, lo que puede ser ineficiente.

**Ejemplos prácticos**: una imagen representada como matriz de píxeles se descompone con SVD y se reconstruye con calidad aceptable conservando solo los valores singulares más grandes, reduciendo el tamaño del archivo. En PLN, LSA usa SVD para identificar patrones y relaciones semánticas entre palabras y documentos, mejorando la recuperación de información y la clasificación de textos.

#### 📌 Espacio Semántico Latente

El Espacio Semántico Latente (ESL) es un modelo matemático y computacional que representa palabras y documentos en un espacio vectorial común. Captura la relación semántica entre términos y textos, facilitando tareas como la recuperación de información, la clasificación de texto y el análisis de sentimientos.

- **Espacio vectorial**: la idea central es representar palabras y documentos como vectores en un espacio de alta dimensión, donde cada dimensión se interpreta como una característica semántica. Así, palabras con significados similares quedan más cerca entre sí.
- **Matriz de co-ocurrencia**: captura la frecuencia con la que las palabras aparecen juntas en un contexto determinado. Se genera a partir de un corpus (filas = palabras, columnas = contextos, p. ej. otras palabras en una ventana de texto) y resulta típicamente muy dispersa y de alta dimensión.
- **SVD sobre la co-ocurrencia**: reduce la dimensionalidad del espacio descomponiendo la matriz en una que representa las palabras, otra que representa los contextos y una matriz diagonal con los valores singulares. Los vectores resultantes capturan las relaciones semánticas más relevantes y se elimina ruido y redundancia.

**Vectores de palabras**: cada palabra es un vector; las que comparten contextos similares tienen vectores más cercanos. Esto captura sinónimos y analogías semánticas (por ejemplo, "rey" es a "reina" como "hombre" es a "mujer").

**Vectores de documentos**: se obtienen agregando los vectores de las palabras que los componen, por promedio o por ponderación según su importancia (por ejemplo, mediante TF-IDF).

**Aplicaciones**: en **recuperación de información**, representar consultas y documentos en el mismo espacio permite hallar documentos semánticamente relevantes aunque no compartan términos exactos. En **clasificación de texto** (correos, comentarios en redes), las relaciones semánticas mejoran la precisión de las predicciones. En **análisis de sentimientos**, ayuda a identificar no solo las palabras explícitas, sino también las relaciones y contextos que indican una opinión positiva o negativa.

### 👾 Proceso de LSA

<p align="center"><img src="assets/img/1980-b.png" alt="Ilustración" width="460"></p>


#### 📌 Construcción de la matriz término-documento

La matriz término-documento (también llamada matriz TF-IDF cuando se aplica una ponderación adicional) es una estructura bidimensional donde las **filas** representan los términos únicos extraídos del conjunto de documentos y las **columnas** representan los documentos individuales. Cada celda contiene la frecuencia de un término en un documento: un conteo simple de ocurrencias o un valor ponderado que refleje su importancia en el contexto de todos los documentos (TF-IDF).

Pasos de construcción:

1. **Recolección de documentos** relevantes y representativos del dominio de interés (textos, artículos, correos electrónicos, etc.).
2. **Preprocesamiento de textos**:
   - **Tokenización**: dividir el texto en términos o tokens (palabras o frases).
   - **Eliminación de *stop words***: filtrar palabras comunes ("y", "el", "de") sin valor semántico significativo.
   - **Lematización o *stemming***: reducir los términos a su forma base o raíz, agrupando variantes de una misma palabra.
3. **Cálculo de frecuencias de términos**:
   - **Frecuencia absoluta**: cuántas veces aparece un término en un documento (si "gato" aparece 5 veces, la frecuencia absoluta es 5).
   - **Frecuencia relativa**: frecuencia absoluta dividida por el número total de términos del documento, para normalizar documentos de distinta longitud.
   - **TF-IDF (Term Frequency–Inverse Document Frequency)**: método más sofisticado que considera la frecuencia del término en el documento y en el conjunto total. Los términos que aparecen en muchos documentos ("el", "y") tienen menos importancia, mientras que los específicos de un documento son más relevantes.

Ejemplo de representación:

| Término | Documento 1 | Documento 2 | Documento 3 |
| ------- | ----------- | ----------- | ----------- |
| gato    | 3           | 0           | 1           |
| perro   | 1           | 2           | 0           |
| pájaro  | 0           | 1           | 1           |

Aquí "gato" aparece 3 veces en el Documento 1, 0 en el 2 y 1 en el 3. Aplicaciones: clasificación de textos (representación numérica para algoritmos de machine learning), búsqueda de información (indexación eficiente de documentos) y análisis de sentimientos (patrones y sentimientos en datos textuales).

#### 📌 Aplicación del SVD: descomponer la matriz y reducir dimensiones

La SVD permite descomponer una matriz en componentes que facilitan la comprensión y manipulación de datos complejos de alta dimensión. Dada una matriz A de dimensión m×n:

```
A  =  U · Σ · Vᵀ

U   ortogonal m×m  → vectores singulares izquierdos
Σ   diagonal m×n   → valores singulares en orden descendente
Vᵀ  transpuesta de V ortogonal n×n → vectores singulares derechos
```

Proceso de descomposición:

```
1. Calcular Aᵀ·A           → matriz cuadrada n×n
2. Valores y vectores propios de Aᵀ·A
                           → valores propios positivos = (valores singulares de A)²
3. Construir V             → vectores propios normalizados de Aᵀ·A
4. Calcular U              → U = A · V · Σ⁻¹     (Σ⁻¹: inversa de la diagonal Σ)
5. Construir Σ             → valores singulares colocados en la diagonal
```

**Reducción de dimensiones.** Una de las aplicaciones más poderosas de la SVD es simplificar la representación de los datos conservando la mayor parte de la información relevante:

1. **Selección de componentes**: tomar los k valores singulares más grandes de Σ y sus columnas correspondientes en U y V, según un umbral que determine cuáles se consideran significativos.
2. **Matrices reducidas**: formar U_k, Σ_k y V_k con solo los k componentes seleccionados.
3. **Reconstrucción aproximada**:

```
A_k  =  U_k · Σ_k · V_kᵀ          (conserva la estructura principal, elimina ruido y redundancia)
```

Ventajas de la reducción: disminuye el impacto del ruido al eliminar componentes menos significativos, facilita la visualización de datos complejos en dimensiones más bajas y acelera los algoritmos de aprendizaje automático al trabajar con matrices de menor dimensión.

#### 📌 Representación vectorial

La representación vectorial transforma palabras, frases y documentos en vectores de un espacio de alta dimensión, facilitando su análisis y manipulación mediante técnicas matemáticas y estadísticas.

- **Vectores y espacios vectoriales**: un vector tiene magnitud y dirección; en PLN, cada palabra o documento se representa como un vector cuyas dimensiones representan características únicas.
- **Dimensionalidad**: número de características usadas para representar la palabra o documento (con 100 dimensiones, cada palabra es un vector de 100 elementos). Una dimensionalidad demasiado baja pierde información; una demasiado alta provoca sobreajuste y aumenta el tiempo de procesamiento.

Métodos de representación:

- **Bolsa de palabras (Bag of Words)**: cada dimensión corresponde a una palabra del vocabulario, con su conteo en el documento o su TF-IDF. *Ventajas*: simplicidad, fácil implementación y eficacia en clasificación de texto. *Desventajas*: ignora el orden de las palabras y no captura relaciones semánticas.
- **Word Embeddings**: representan palabras de forma que las de significado similar queden más cerca.
  - **Word2Vec**: usa redes neuronales para aprender representaciones a partir de grandes corpus. Tiene dos arquitecturas: **CBOW** (Continuous Bag of Words), que predice una palabra a partir de su contexto, y **Skip-Gram**, que hace lo contrario.
  - **GloVe** (Global Vectors for Word Representation): se basa en la matriz de coocurrencia de palabras, captura información global del corpus y produce vectores en un espacio semántico.
- **Representación de documentos**: media de los vectores de sus palabras, o modelos más complejos como **Doc2Vec**, que extiende Word2Vec a documentos completos.

Aplicaciones: **clasificación de texto** (los vectores de características alimentan modelos como SVM, Naive Bayes o redes neuronales), **búsqueda semántica** (similitud entre vectores mediante la distancia coseno, para recuperar documentos semánticamente relevantes) y **análisis de sentimiento** (patrones del lenguaje asociados a opiniones positivas o negativas).

Desafíos: necesidad de grandes cantidades de datos para entrenar modelos efectivos, dificultad para capturar el contexto y la ambigüedad del lenguaje, y la representación de distintos idiomas y dialectos. La investigación futura busca entender mejor el contexto y las relaciones semánticas, y crear representaciones más eficientes para aplicaciones de PLN en tiempo real.

### 👾 El impacto de esta técnica en la comprensión automática del lenguaje

<p align="center"><img src="assets/img/1980-c.png" alt="Ilustración" width="460"></p>


#### 📌 Mejoras en recuperación de información

##### Sinónimos y polisemia

Relacionar términos similares y desambiguar significados es clave para mejorar la comprensión del lenguaje y la interacción humano-máquina.

- **Sinónimos**: palabras o expresiones de significado similar o idéntico en ciertos contextos; permiten variar el lenguaje y evitar la repetición (por ejemplo, "feliz", "contento" y "alegre" al describir un estado emocional positivo).
  - **Absolutos**: intercambiables en cualquier contexto sin alterar el significado ("coche" y "automóvil").
  - **Parciales**: significado similar pero no intercambiables en todos los contextos; "casa" se refiere a la estructura física, mientras que "hogar" conlleva una connotación emocional.
- **Polisemia**: capacidad de una palabra para tener múltiples significados, frecuente fuente de ambigüedad ("banco": institución financiera u objeto para sentarse).
  - **Desambiguación** mediante el **contexto lingüístico** (las palabras que rodean a la palabra polisémica dan pistas: en "Fui al banco a retirar dinero", el contexto financiero indica la institución) o mediante **métodos basados en datos** (algoritmos de aprendizaje automático y modelos como Word2Vec o BERT que aprenden patrones de uso para identificar el significado más probable).

Importancia en PLN: la correcta identificación de sinónimos y la desambiguación mejoran la **traducción automática**, el **análisis de sentimientos** y los **sistemas de recomendación**, al comprender mejor las preferencias del usuario a través de sinónimos y distintos significados.

##### Consultas más efectivas

La calidad de los resultados depende en gran medida de cómo se estructuran y formulan las consultas.

- **Semántica de la consulta**: entender cómo el motor interpreta el lenguaje natural exige **desambiguar** palabras con múltiples interpretaciones y considerar el **contexto**, que puede cambiar su significado.
- **Estructura de la consulta**: usar palabras clave relevantes y específicas; con frecuencia, las frases completas o preguntas generan resultados más relevantes que palabras sueltas.

Estrategias:

- **Especificidad**: en lugar de "perros", una consulta más efectiva es "mejores razas de perros para familias con niños".
- **Operadores booleanos**: **AND** incluye ambos términos ("perros AND entrenamiento"); **OR** incluye cualquiera ("perros OR gatos"); **NOT** excluye uno ("perros NOT bulldogs").
- **Frases exactas y comillas**: "cuidado de perros" devuelve resultados con esa secuencia exacta.
- **Sinónimos y variaciones**: además de "comprar coche", probar "adquirir automóvil" amplía los resultados.

La evaluación de resultados atiende a su **relevancia** (pertinencia a la consulta) y **precisión** (exactitud frente a las expectativas del usuario), ajustando las consultas de forma iterativa: cambiar palabras clave, reestructurar o experimentar con operadores.

#### 📌 Aplicaciones en educación

##### Evaluación automática de ensayos

Usa algoritmos y modelos computacionales para analizar la calidad y el contenido de los textos de los estudiantes, comparándolos con materiales de referencia mediante el análisis de similitud entre textos.

La **similitud de textos** mide en qué grado dos o más textos comparten contenido o significado:

- **Similitud léxica**: coincidencia en el vocabulario, con técnicas como la distancia de Levenshtein o el coeficiente de Jaccard.
- **Similitud semántica**: evalúa el significado con Word2Vec, GloVe y modelos basados en transformadores (por ejemplo, BERT), capturando relaciones más profundas.

Técnicas de evaluación: análisis basado en reglas (búsqueda de frases o estructuras gramaticales predefinidas), modelos de aprendizaje automático (clasificación y regresión entrenados sobre datos etiquetados) y redes neuronales profundas (LSTM, Transformers, con comprensión contextual del texto).

Tras el preprocesamiento (tokenización, lematización/stemming y eliminación de *stop words*), se calcula la similitud:

- **Cosine Similarity**: coseno del ángulo entre dos vectores, independiente de la longitud de los textos.
- **Similitud de Jaccard**: tamaño de la intersección dividido por el de la unión de dos conjuntos.
- **Similitud semántica basada en embeddings**: distancia entre vectores generados con Word2Vec o BERT.

Desafíos: la **ambigüedad y polisemia** (los modelos deben contextualizar el uso de las palabras), el **estilo y la creatividad** (reconocer la originalidad sin penalizar en exceso las diferencias estilísticas) y el **sesgo en los datos** (los modelos heredan sesgos del entrenamiento, por lo que se requieren conjuntos diversos y representativos).

##### Herramientas de tutoría inteligente

Las herramientas de tutoría inteligente (ITS, Intelligent Tutoring Systems) ofrecen una experiencia educativa personalizada, adaptando contenido y estrategias a las necesidades de cada estudiante mediante PLN y aprendizaje automático.

- **Personalización del aprendizaje**: analizan el rendimiento en tiempo real, identifican fortalezas y debilidades y adaptan contenido, dificultad y tipo de actividades, ofreciendo recursos adicionales (ejercicios, lecturas) en las áreas a mejorar.
- **Evaluación continua**: pruebas cortas, cuestionarios y ejercicios interactivos cuyos resultados permiten ajustes dinámicos; si el estudiante muestra dificultades en un concepto, el sistema añade ejemplos y explicaciones antes de avanzar.
- **Retroalimentación inmediata**: ante un error, ofrece explicaciones y sugerencias instantáneas, lo que corrige en el momento y fomenta un aprendizaje más profundo mediante la reflexión.

Tecnologías: el **PLN** interpreta y analiza las respuestas del estudiante, identifica patrones y mide su nivel de comprensión para ajustar la dificultad; el **aprendizaje automático** refina los algoritmos a partir de las interacciones para predecir qué contenido será más útil.

Ejemplos de herramientas:

1. **Knewton**: usa algoritmos de aprendizaje adaptativo para personalizar el contenido según el rendimiento y el estilo de aprendizaje.
2. **Duolingo**: en aprendizaje de idiomas, adapta las lecciones al progreso del usuario, ajustando la dificultad y reforzando las áreas más débiles.
3. **ALEKS**: en matemáticas, evalúa el conocimiento con un enfoque adaptativo, identifica los conceptos dominados y los que requieren atención y ofrece un camino de aprendizaje optimizado.

#### 📌 Avances en procesamiento del lenguaje natural

##### Traducción automática

La traducción automática (TA) convierte texto de un idioma a otro mediante algoritmos y modelos. La **alineación** empareja segmentos del idioma origen con sus equivalentes en el destino, garantizando que la traducción sea correcta y conserve el significado:

- **A nivel de palabra**: empareja palabras individuales; útil, pero a menudo insuficiente porque ignora el contexto más amplio de las frases.
- **A nivel de frase**: empareja bloques mayores, como oraciones o frases completas, capturando mejor las relaciones semánticas y sintácticas y produciendo traducciones más coherentes y naturales.

Una alineación efectiva aporta **precisión** (mejor comprensión del contexto, menos errores), **fluidez** (respeto de las estructuras gramaticales del idioma destino) y **consistencia** terminológica, especialmente importante en textos técnicos.

Métodos de mejora:

- **Modelos estadísticos**: los modelos basados en frases (Phrase-Based Models) aprenden patrones de alineación a partir de grandes corpus paralelos y de la frecuencia de aparición de frases, estableciendo probabilidades de alineación; su limitación es que captan mal las complejidades semánticas.
- **Aprendizaje profundo**: redes neuronales recurrentes (RNN) y transformadores aprenden representaciones más complejas entre frases y términos. Los **transformadores**, introducidos por Vaswani et al. en 2017, revolucionaron la TA: capturan dependencias a largo plazo y, mediante el mecanismo de atención, enfocan distintas partes de la entrada al generar la salida, mejorando precisión y fluidez.
- **Alineación contextual**: enfoque más reciente que usa modelos preentrenados (BERT, GPT) para entender el significado según el contexto, útil ante palabras o frases con múltiples significados.

Evaluación de la alineación:

- **BLEU (Bilingual Evaluation Understudy)**: mide la coincidencia de n-gramas con una o más traducciones de referencia; ampliamente usado, pero limitado para captar fluidez y adecuación semántica.
- **METEOR (Metric for Evaluation of Translation with Explicit ORdering)**: considera sinónimos y variaciones morfológicas, permitiendo una evaluación más precisa.
- **TER (Translation Edit Rate)**: mide las ediciones necesarias para transformar la traducción en la referencia; un TER más bajo indica mejor alineación y calidad.

##### Resumen automático

Condensa textos extensos extrayendo las ideas más relevantes, esencial ante el crecimiento exponencial de la información.

- **Resumen extractivo**: selecciona y extrae las oraciones más relevantes del texto original, reutilizándolas para formar un resumen coherente.
  - *Métodos*: frecuencia de términos (TF-IDF) para identificar oraciones con términos significativos, y algoritmos de puntuación como PageRank adaptado para evaluar la importancia de las oraciones.
  - *Ventajas*: mantiene la integridad del original, es más fácil de implementar y menos propenso a errores semánticos.
  - *Desventajas*: puede carecer de fluidez y no captar el contexto general del documento.
- **Resumen abstractivo**: genera un texto nuevo que parafrasea y sintetiza la información, lo que exige comprensión profunda del contenido.
  - *Métodos*: modelos de aprendizaje profundo como Transformers (BERT, GPT) y técnicas de generación con mecanismos de atención.
  - *Ventajas*: resúmenes más coherentes y legibles, que pueden incluir información no explícita en el original.
  - *Desventajas*: mayor complejidad computacional y riesgo de generar información incorrecta o incoherente.

Evaluación: métodos automáticos como **ROUGE** (compara la superposición de n-gramas con un resumen de referencia) y **BLEU** (proveniente de la TA); y evaluación humana de coherencia, relevancia y fluidez.

Aplicaciones: medios de comunicación (resúmenes de artículos para lectura rápida), investigación académica (resúmenes de trabajos científicos para identificar estudios relevantes) y asistentes virtuales (resúmenes de correos y documentos). Desafíos: la ambigüedad del lenguaje y la necesidad de contextualización.

#### 📌 Limitaciones y críticas

##### Requerimientos computacionales

Se considera un **gran corpus** aquel que contiene millones o miles de millones de palabras (Common Crawl, Wikipedia, grandes colecciones académicas o de redes sociales), lo que plantea retos de almacenamiento, procesamiento y análisis.

- **Almacenamiento**: los corpus ocupan desde varios gigabytes hasta terabytes. Conviene usar sistemas de archivos distribuidos o bases NoSQL —como Hadoop Distributed File System (HDFS) o MongoDB— y formatos eficientes (JSON, Parquet o Avro), que optimizan el acceso frente a formatos simples como CSV.
- **Procesamiento**: las **GPU** aceleran el entrenamiento de modelos complejos mediante cálculo en paralelo, mientras que las **CPU** son más adecuadas para tareas secuenciales. La **memoria RAM** es crítica: se recomiendan al menos 16 GB para tareas básicas y 64 GB o más para tareas intensivas.
- **Software**: frameworks como TensorFlow, PyTorch y spaCy, optimizados para el hardware disponible, junto con la optimización de algoritmos (reducción de dimensionalidad, muestreo de datos y aprendizaje en línea que se actualiza sin reentrenar desde cero).
- **Escalabilidad y distribución**: la computación distribuida (Apache Spark) procesa datos en paralelo a través de múltiples nodos, superando la capacidad de un solo sistema; una carga de trabajo equilibrada evita cuellos de botella y maximiza el uso de recursos.

##### Estática del modelo

Los modelos estáticos se entrenan sobre un conjunto de datos específico y fijan su estructura y parámetros tras el entrenamiento, de modo que cualquier cambio en los datos exige un nuevo ciclo de entrenamiento, intensivo en tiempo y recursos.

- **Costos computacionales**: reentrenar desde cero, sobre todo con redes neuronales profundas, requiere mucho hardware (GPU) y tiempo de convergencia; poco práctico cuando la velocidad de actualización es crítica, como en sistemas de recomendación o chatbots que interactúan en tiempo real.
- **Desactualización**: sin integrar nuevos datos, los modelos se vuelven obsoletos y dejan de reflejar patrones y tendencias actuales, algo especialmente relevante en contextos cambiantes como el análisis de sentimientos en redes sociales, lo que degrada el rendimiento.
- **Estrategias de mitigación**:
  - **Aprendizaje incremental**: actualiza el modelo de forma continua ajustando solo los parámetros necesarios para incorporar la nueva información, sin reentrenar todo; difícil de implementar y no siempre efectivo según el tipo de modelo.
  - **Transferencia de aprendizaje**: parte de un modelo preentrenado y lo ajusta con un conjunto más pequeño y específico, reduciendo el tiempo de entrenamiento y permitiendo adaptarse a nuevos contextos sin empezar de cero.
  - **Modelos de ensembles**: combinan múltiples modelos entrenados en distintos conjuntos de datos para mejorar la robustez y la capacidad de adaptación, seleccionando el más adecuado según la situación.

### 👾 Conclusión

<p align="center"><img src="assets/img/1980-d.png" alt="Ilustración" width="460"></p>


El LSA, propuesto formalmente por Deerwester et al. (1990) a partir de ideas gestadas en los años 80, marcó un punto de inflexión al representar términos y documentos en un espacio semántico común mediante la SVD aplicada a la matriz término-documento, superando la rigidez de las búsquedas por palabras clave y abordando los problemas de sinónimos y polisemia. Sus aplicaciones se extienden a la recuperación de información, a la educación —con la evaluación automática de ensayos y la tutoría inteligente (Knewton, Duolingo, ALEKS)— y a avances del PLN como la traducción automática, impulsada por los transformadores de Vaswani et al. (2017) y evaluada con BLEU, METEOR y TER, y el resumen automático extractivo y abstractivo, evaluado con ROUGE y BLEU. Sus principales limitaciones son el alto costo computacional sobre grandes corpus y la estática del modelo, mitigable mediante aprendizaje incremental, transferencia de aprendizaje y ensembles. Con ello, el LSA sentó las bases conceptuales de los modelos semánticos y embeddings posteriores —Word2Vec, GloVe, BERT y GPT— que hoy dominan la comprensión automática del lenguaje.

> [!TIP] 😄 Pausa
> LSA descompone el significado en valores singulares. Yo me descompongo en cualquier reunión antes de las 9 am.

## 🏠 Década de 1990: Redes Neuronales y Representaciones Distribuidas

<p align="center"><img src="assets/img/1990-a.png" alt="Ilustración" width="460"></p>


### 👾 Uso Temprano de Redes Neuronales para Representaciones Distribuidas

> [!TIP] 😄 Pausa
> Backpropagation: aprender de los errores propagándolos hacia atrás. Algo que los humanos llevamos haciendo mal desde siempre.


#### 📌 Renacimiento de las Redes Neuronales

##### Backpropagation (retropropagación)

La retropropagación es el algoritmo que permite a las redes neuronales ajustar sus pesos y sesgos durante el entrenamiento. Se basa en el cálculo del gradiente y fue clave en la popularización de las redes neuronales desde la década de 1980.

**Historia y contexto.** El concepto fue introducido por primera vez en 1974 por Paul Werbos. Sin embargo, ganó atención generalizada con el artículo "Learning representations by back-propagating errors", de Geoffrey Hinton, David Rumelhart y Ronald Williams (1986), que demostró que la retropropagación podía entrenar redes neuronales multicapa, abriendo la puerta a aplicaciones complejas en procesamiento de señales y reconocimiento de patrones.

**Fundamentos.** El objetivo es minimizar una función de pérdida que mide la discrepancia entre las predicciones de la red y los valores reales. El proceso consta de dos fases:

1. **Propagación hacia adelante**: se calcula la salida de la red; los datos pasan por las capas y en cada una se aplican funciones de activación que introducen no linealidades.
2. **Retropropagación**: con la salida obtenida, se calcula el error mediante la función de pérdida y se propaga hacia atrás, calculando el gradiente de la pérdida respecto a cada peso y sesgo mediante la regla de la cadena.

**Implementación.**

1. **Inicialización** aleatoria de pesos y sesgos.
2. **Cálculo de la salida** mediante propagación hacia adelante.
3. **Cálculo del error** con una función de pérdida adecuada (error cuadrático medio para regresión, entropía cruzada para clasificación).
4. **Cálculo de gradientes** mediante derivadas parciales.
5. **Actualización de parámetros** con un algoritmo de optimización como el descenso de gradiente.

**Ventajas:**
- **Eficiencia computacional**: cálculo eficiente de gradientes, crucial para redes con muchos parámetros.
- **Flexibilidad**: aplicable a perceptrones multicapa, redes convolucionales y recurrentes.

**Desventajas:**
- **Problemas de convergencia**, especialmente en redes profundas, donde aparecen gradientes vanishing o exploding.
- **Dependencia de la inicialización** de los pesos, que afecta significativamente el rendimiento.

La retropropagación ha sido un pilar del aprendizaje profundo, con avances en visión por computadora, procesamiento del lenguaje natural y robótica.

##### Modelos conexistas

Los modelos conexistas, o modelos basados en redes neuronales, simulan procesos cognitivos humanos mediante redes neuronales artificiales inspiradas en la estructura y funcionalidad del cerebro.

**Principios fundamentales.** El conocimiento se representa y procesa a través de conexiones entre unidades simples (neuronas), organizadas en capas. La activación de una neurona depende de la suma ponderada de las señales que recibe, lo que permite a la red representar patrones complejos modificando las conexiones (pesos). El aprendizaje se realiza mediante ajuste de pesos, siendo el más conocido la retropropagación: la red ajusta sus pesos según el error en la predicción y mejora su capacidad de generalizar a nuevos datos.

**Arquitecturas de redes neuronales.**

- **Redes Neuronales Artificiales (ANN)**: forma más básica, con una capa de entrada, una o más capas ocultas y una de salida. Realizan clasificación y regresión; en PLN se usan para clasificación de texto y análisis de sentimientos.
- **Redes Neuronales Convolucionales (CNN)**: efectivas con datos en estructura de grid (imágenes, texto). Usan capas convolucionales que detectan patrones locales.
- **Redes Neuronales Recurrentes (RNN)**: procesan secuencias; mantienen un estado interno que recuerda entradas anteriores, útil para traducción automática y modelado de lenguaje.
- **Transformers**: usan mecanismos de atención para enfocarse en distintas partes de la entrada, mejorando la traducción y la generación de texto.

**Aplicaciones en procesos cognitivos:** reconocimiento de patrones (identificar patrones en datos complejos), procesamiento del lenguaje natural (traducción automática, análisis de sentimientos, generación de texto) y simulación de procesos cognitivos como memoria, aprendizaje y toma de decisiones.

#### 📌 Representaciones Distribuidas

##### Concepto: representar información mediante patrones de activación

La representación de información en PLN evolucionó con las redes neuronales. Una idea central es representar información mediante patrones de activación, lo que captura la complejidad del lenguaje humano de un modo que los métodos tradicionales no lograban.

Las redes neuronales se componen de capas de nodos (neuronas) interconectados. Cada neurona recibe entradas, las procesa y produce una salida. La activación es el valor resultante de aplicar una función de activación a la suma ponderada de las entradas.

- **Función de activación**: funciones como la sigmoide, ReLU (Rectified Linear Unit) y la tangente hiperbólica transforman la entrada en una salida usable por la siguiente capa, introduciendo no linealidades esenciales para aprender patrones complejos.
- **Patrones de activación**: forma en que las neuronas se activan ante distintas entradas. En PLN se interpretan como representaciones semánticas de palabras, frases o documentos; al entrenarse la red, se ajustan para reflejar relaciones y similitudes entre conceptos lingüísticos.

**Representación semántica.** Permite capturar significados contextuales y relaciones semánticas mediante:

- **Word Embeddings**: Word2Vec y GloVe crean representaciones densas de palabras en un espacio vectorial, donde palabras con significados similares quedan más cercanas. Se generan a partir de patrones de activación en redes entrenadas sobre grandes corpus.
- **Transformers**: BERT y GPT usan arquitecturas de atención; sus patrones de activación representan palabras y capturan también el contexto, logrando una comprensión más rica del lenguaje.

El entrenamiento optimiza los pesos de conexión para minimizar la diferencia entre salidas predichas y reales; los patrones de activación se vuelven más precisos y la red generaliza a datos no vistos.

##### Ventajas: generalizar y manejar información incompleta

La capacidad de generalizar y manejar información incompleta es una característica destacada de los modelos de PLN, fundamental en traducción automática, análisis de sentimientos y respuesta a preguntas.

**Generalización**: aplicar lo aprendido a ejemplos no vistos.

1. **Adaptación a nuevos contextos**: un modelo que generaliza bien se adapta a nuevos dominios sin reentrenamiento exhaustivo (p. ej., un modelo entrenado en noticias puede analizar textos de redes sociales si aprendió patrones semánticos y sintácticos relevantes).
2. **Reducción de overfitting**: mitiga el ajuste excesivo a los datos de entrenamiento, dando modelos más robustos y confiables.
3. **Mejora de la interpretabilidad**: ofrece explicaciones más claras de sus decisiones (p. ej., palabras indicativas de sentimiento positivo en varios contextos).

**Manejo de información incompleta**: los datos suelen ser ruidosos, incompletos o ambiguos.

1. **Robustez ante datos ruidosos**: infiere, por ejemplo, el sentimiento general aunque partes del texto falten o sean contradictorias.
2. **Inferencia y razonamiento**: deduce información implícita, dando respuestas más precisas aun cuando la pregunta no contiene todos los detalles.
3. **Mejoras en la experiencia del usuario**: en aplicaciones interactivas, completar información faltante favorece interacciones exitosas cuando el usuario no formula sus preguntas de forma completa.

#### 📌 Modelos Pioneros

##### Redes de Hopfield: memoria asociativa

Las redes de Hopfield son redes neuronales recurrentes usadas como modelos de memoria asociativa. Fueron introducidas por John Hopfield en 1982 y destacan por almacenar patrones y recuperarlos eficientemente incluso con ruido o datos incompletos. Se han aplicado desde la inteligencia artificial hasta la neurociencia.

**Estructura.** Conjunto de neuronas conectadas entre sí; cada neurona está activada (1) o desactivada (0). Las conexiones son sinápticas, con pesos simétricos y sin auto-conexiones (una neurona no se conecta a sí misma).

**Representación de patrones.** Los pesos se asignan según el patrón a memorizar. Para un patrón de `p` bits se necesitan al menos `p` neuronas. Los pesos se calculan con la regla de Hebb: la conexión entre dos neuronas se fortalece cuando ambas se activan simultáneamente.

**Matriz de pesos** `W`, donde ξ^k es el k-ésimo patrón a almacenar y N el número total de neuronas:

```
W_ij = 0                                  si i = j
W_ij = (1/N) · Σ_{k=1..p} ξ_i^k · ξ_j^k    si i ≠ j
```

**Dinámica: actualización de estados.** El estado se actualiza de forma asincrónica: en cada iteración se selecciona una neurona al azar y se calcula su nuevo estado, donde s_i(t) es el estado de la neurona i en el tiempo t y sign devuelve 1 si el argumento es positivo y −1 si es negativo:

```
s_i(t+1) = sign( Σ_{j ≠ i} W_ij · s_j(t) )
```

**Convergencia y estabilidad.** La red converge a un estado estable correspondiente a uno de los patrones almacenados, asemejándose a la minimización de una función de energía hacia un mínimo local. La energía se define como:

```
E = -(1/2) · Σ_{i ≠ j} W_ij · s_i · s_j
```

La red evoluciona hacia configuraciones de menor energía y se estabiliza en uno de los patrones almacenados.

**Propiedades.**
- **Capacidad de almacenamiento** limitada: el máximo de patrones sin interferencia es aproximadamente `0.15 · N`, donde N es el número de neuronas.
- **Robustez ante ruido**: ante un patrón de entrada ruidoso, la red converge al patrón original más cercano por su naturaleza asociativa.

**Aplicaciones:** reconocimiento de patrones en datos ruidosos o incompletos; optimización combinatoria (p. ej., el problema del vendedor viajero); modelado de memoria (cómo se almacenan y recuperan recuerdos en el cerebro humano).

##### Modelos de Elman y Jordan: redes recurrentes para secuencias temporales

Las redes neuronales recurrentes (RNN) procesan datos secuenciales como texto o series temporales. Los modelos de Elman y Jordan son arquitecturas fundamentales que introdujeron mecanismos para que las redes "recuerden" información de entradas anteriores, crucial para el contexto en secuencias temporales.

**Modelo de Elman** (Jeffrey Elman, 1990). Red feedforward con un componente recurrente:

- **Capa de entrada**: recibe las entradas de la secuencia temporal.
- **Capa oculta**: procesa la información y genera activaciones.
- **Capa de salida**: produce la salida de la entrada actual.

Su rasgo distintivo es la **capa de contexto**, que almacena las activaciones de la capa oculta del tiempo anterior y las retroalimenta a la capa oculta en el siguiente paso, permitiendo usar información pasada.

Funcionamiento: (1) propagación hacia adelante, combinando la entrada actual con las activaciones de la capa de contexto; (2) cálculo de salida desde la capa oculta; (3) retropropagación a través del tiempo (BPTT) para actualizar los pesos considerando entradas actuales y pasadas. Es sencillo y fácil de entrenar, pero sufre desvanecimiento y explosión del gradiente, lo que dificulta el aprendizaje en secuencias largas.

**Modelo de Jordan** (misma época). Arquitectura similar, pero retroalimenta las **salidas** de la red como entradas del siguiente paso, en lugar de las activaciones de la capa oculta:

- **Capa de entrada**: similar a Elman.
- **Capa oculta**: procesa la entrada.
- **Capa de salida**: genera la salida y se retroalimenta a la capa de entrada en el siguiente paso.

Funcionamiento: (1) la red toma la entrada actual y la salida del paso anterior; (2) cálculo de salida desde la capa oculta; (3) BPTT para actualizar los pesos. Es útil cuando la salida anterior influye en la entrada actual, como en la generación de texto, pero también enfrenta desvanecimiento y explosión del gradiente.

**Comparación:**

| Característica    | Modelo de Elman                           | Modelo de Jordan                          |
| ----------------- | ----------------------------------------- | ----------------------------------------- |
| Retroalimentación | Capa de contexto (activaciones)           | Salida anterior                           |
| Aplicaciones      | Predicción de secuencias                  | Generación de texto y secuencias          |
| Problemas         | Desvanecimiento y explosión del gradiente | Desvanecimiento y explosión del gradiente |

Ambos son hitos en las RNN y sentaron las bases de arquitecturas más avanzadas como LSTM (Long Short-Term Memory) y GRU (Gated Recurrent Unit).

### 👾 Avances y Limitaciones frente a Enfoques Posteriores

<p align="center"><img src="assets/img/1990-b.png" alt="Ilustración" width="460"></p>


#### 📌 Aplicaciones en Lenguaje

##### Modelado del lenguaje: predicción de la palabra siguiente

El modelado del lenguaje se centra en comprender y generar texto; una de sus aplicaciones más comunes es predecir la siguiente palabra en una secuencia, esencial para traducción automática, resumen y respuesta a preguntas.

**Conceptos fundamentales.**

- **Secuencias de palabras**: serie de tokens (p. ej., en "El gato está en el tejado", cada palabra es un token).
- **Probabilidades condicionales**: el objetivo es calcular la probabilidad de una palabra en un contexto, donde w_n es la palabra a predecir y w_1...w_{n-1} las anteriores:

```
P( w_n | w_1, w_2, ..., w_{n-1} )
```

- **Modelos N-gram**: usan la cadena de Markov para estimar la probabilidad de la siguiente palabra a partir de las n−1 anteriores. Se definen modelos bigram (n=2), trigram (n=3), etc.:

```
P( w_n | w_{n-1} )              modelo bigram
P( w_n | w_{n-2}, w_{n-1} )     modelo trigram
```

- **Limitaciones de los N-gram**: escalabilidad (al crecer n, las combinaciones crecen exponencialmente y requieren más datos); sparsity (muchos N-grams no aparecen en el corpus); contexto limitado (solo consideran un número fijo de palabras anteriores).

**Modelos basados en redes neuronales.**

- **Word Embeddings**: Word2Vec y GloVe representan palabras en un espacio vectorial continuo capturando relaciones semánticas y sintácticas.
- **RNN**: trabajan con secuencias de longitud variable y mantienen un estado interno con información de palabras anteriores.
- **LSTM y GRU**: variantes de RNN que abordan el desvanecimiento del gradiente y permiten aprender dependencias a largo plazo.
- **Transformers**: con mecanismos de atención, capturan relaciones complejas y contextos amplios sin las limitaciones de las RNN.

**Evaluación.** Se usa comúnmente la **perplejidad**, que mide la capacidad del modelo para predecir una muestra de texto; menor perplejidad indica mejor rendimiento.

##### Desambiguación lexical

La desambiguación lexical determina el significado correcto de una palabra polisémica según su contexto, esencial para que las máquinas interpreten el lenguaje natural.

La ambigüedad lexical es común: "banco" puede referirse a una institución financiera o a un asiento. Sin desambiguación, los sistemas de PLN generan errores en traducción automática, recuperación de información y análisis de sentimientos.

**Métodos basados en el conocimiento** (recursos lexicográficos):
- **WordNet**: base de datos léxica del inglés que agrupa palabras en conjuntos de sinónimos (synsets) y aporta definiciones y relaciones semánticas; permite hallar el synset más relevante.
- **Ontologías**: representaciones formales de conceptos de un dominio y sus relaciones, que aportan contexto semántico más rico.

**Métodos basados en datos** (aprendizaje automático y estadística):
- **Modelos de clasificación**: modelos supervisados con características contextuales (palabras circundantes), como Support Vector Machines (SVM) y Random Forests.
- **Word Embeddings**: Word2Vec y GloVe sitúan palabras de significado similar cerca en un espacio semántico, ayudando a capturar el contexto.
- **Modelos basados en transformadores**: BERT y GPT representan las palabras según su contexto inmediato, mejorando la precisión.

**Evaluación.** Mediante conjuntos de datos anotados con los significados correctos; las métricas incluyen precisión, recuperación y F1-score.

**Desafíos**: ambigüedad contextual (el contexto a veces no basta); variabilidad del lenguaje (evoluciona y reduce la relevancia de modelos antiguos); recursos limitados para idiomas menos comunes (la mayoría están diseñados para el inglés).

#### 📌 Limitaciones

##### Capacidad computacional: entrenamiento lento y grandes volúmenes de datos

La capacidad computacional es un desafío persistente, visible en el entrenamiento lento de modelos y la gestión de grandes volúmenes de datos.

**Entrenamiento lento.**

1. **Complejidad de los modelos**: los modelos basados en redes neuronales profundas pueden tener millones o miles de millones de parámetros. Modelos como BERT y GPT-3 requieren tiempo significativo para converger.
2. **Costos computacionales**: el uso de GPU o TPU para acelerar el entrenamiento puede ser prohibitivamente caro, generando una brecha de accesibilidad.
3. **Tamaño del conjunto de datos**: a mayor complejidad, mayores conjuntos de datos; su recolección, limpieza y preprocesamiento exigen tiempo y esfuerzo.
4. **Optimización del entrenamiento**: técnicas de paralelización y algoritmos de optimización más eficientes requieren comprensión profunda de la arquitectura y la infraestructura.

**Grandes volúmenes de datos.**

1. **Almacenamiento y gestión**: el crecimiento exponencial de los datos obliga a soluciones de almacenamiento distribuidas y escalables.
2. **Sesgo y representatividad**: los grandes volúmenes pueden introducir sesgos; hay que asegurar que los datos sean representativos de la diversidad del lenguaje.
3. **Ruido en los datos**: los conjuntos grandes contienen datos irrelevantes o incorrectos cuya identificación y eliminación es laboriosa.
4. **Escalabilidad del modelo**: el modelo debe manejar más datos y aprender de ellos eficientemente, factor crítico en entornos reales.

##### Vanishing Gradient: dificultad para entrenar redes profundas

El vanishing gradient ocurre cuando los gradientes de los pesos se vuelven extremadamente pequeños al retropropagarse por las capas, de modo que las capas cercanas a la entrada reciben actualizaciones mínimas y no aprenden representaciones complejas.

**Retropropagación y gradientes.** La retropropagación calcula el gradiente de la pérdida respecto a cada peso mediante la regla de la cadena, multiplicando gradientes a través de las capas. En redes profundas esta multiplicación puede volver los gradientes muy pequeños (vanishing) o muy grandes (exploding).

**Causas.** Se debe principalmente a funciones de activación como la sigmoide y la tangente hiperbólica (tanh), cuyas derivadas son pequeñas en los extremos de su rango; en redes profundas los gradientes disminuyen exponencialmente.

**Ejemplo.** En una red con capas ocultas y activación sigmoide, si una neurona está en la parte plana de la sigmoide (cerca de 0 o 1), su derivada es cercana a 0; el producto de derivadas tiende a cero y los pesos de esa capa apenas se actualizan.

**Consecuencias:**
1. **Dificultad para entrenar redes profundas**: las capas iniciales no aprenden adecuadamente.
2. **Suboptimización**: la red converge a un mínimo local no óptimo.
3. **Inestabilidad**: unas capas aprenden y otras no, dando rendimiento inconsistente.

**Soluciones:**
1. **Funciones de activación alternativas**: ReLU y variantes (Leaky ReLU, Parametric ReLU), menos propensas al vanishing gradient.
2. **Inicialización adecuada de pesos**: inicialización de He o de Xavier.
3. **Arquitecturas alternativas**: redes residuales (ResNets) con conexiones de salto que dejan fluir los gradientes.
4. **Técnicas de normalización**: normalización por lotes (Batch Normalization) para estabilizar y acelerar el entrenamiento.

#### 📌 Comparación con Enfoques Posteriores

##### Frente a Word2Vec y modelos actuales

Word2Vec, introducido por Mikolov et al. en 2013, marcó un hito en PLN al representar palabras en un espacio vectorial de forma eficiente mediante Continuous Bag of Words (CBOW) y Skip-Gram, capturando relaciones semánticas y sintácticas por proximidad. Aun así, presenta limitaciones frente a modelos más recientes.

**Limitaciones de Word2Vec:**
1. **Representación estática**: cada palabra tiene un único vector independiente del contexto, de modo que las palabras polisémicas comparten un mismo vector, generando confusiones en desambiguación.
2. **Captura de contexto limitada**: usa una ventana de contexto fija, limitando las relaciones complejas y las dependencias a largo plazo.
3. **Escalabilidad y eficiencia**: con grandes vocabularios o conjuntos de datos, calcular similitudes entre todos los vectores resulta costoso.

**Modelos actuales y sus ventajas:**
1. **Embeddings contextuales**: ELMo, BERT y GPT generan representaciones que cambian según el contexto (p. ej., "banco" en "banco de peces" frente a "banco de dinero"), mejorando la desambiguación.
2. **Arquitecturas de atención**: los Transformers capturan relaciones a larga distancia, dando representaciones más ricas y matizadas.
3. **Transferencia de aprendizaje**: modelos preentrenados como BERT y GPT se entrenan en grandes corpus y luego se ajustan a tareas específicas, frente a Word2Vec, que entrena desde cero para cada tarea.

**Comparación.** En eficiencia, Word2Vec es eficiente en su contexto pero su enfoque estático y el cálculo de similitudes por tarea lo limitan a gran escala; los modelos actuales, aunque más costosos en recursos, reutilizan embeddings contextuales y escalan mediante transferencia de aprendizaje. En capacidad de representación, Word2Vec ofrece una representación semántica básica sin capturar contexto ni polisemia, mientras que los modelos actuales aportan representaciones ricas y dinámicas adaptables al contexto.

##### Aprendizaje no supervisado

En los 90 predominaban los métodos supervisados, lo que limitaba la escalabilidad y la flexibilidad. El aprendizaje no supervisado surgió como alternativa, permitiendo aprender de datos sin etiquetas predefinidas.

**Definición y características.** Algoritmos que extraen patrones de un conjunto de datos sin etiquetas, descubriendo estructuras subyacentes:
- **Exploración de datos**: identifica patrones, tendencias y agrupaciones sin supervisión.
- **Reducción de dimensionalidad**: técnicas como PCA (Análisis de Componentes Principales) simplifican los datos manteniendo su esencia.
- **Agrupamiento**: K-means y DBSCAN segmentan los datos en grupos según similitudes.

**Contexto histórico.** En los 90 predominaba el aprendizaje supervisado por la disponibilidad de datos etiquetados, pero presentaba desafíos: requerimiento de datos etiquetados (costoso y laborioso); adaptabilidad limitada ante cambios de dominio (exige reentrenamiento); sobrecarga de información (etiquetar cada instancia es impráctico con grandes volúmenes).

**Avances:**
- **Algoritmos de clustering mejorados**: clustering jerárquico y basado en densidad.
- **Modelos generativos**: Redes Generativas Antagónicas (GANs) y Modelos de Mezcla Gaussiana (GMM) generan nuevos datos a partir de patrones aprendidos.
- **Aprendizaje profundo**: combinado con métodos no supervisados, permite extracción automática de características y representación de datos de alta dimensión.

**Aplicaciones:** análisis de clientes (segmentación en marketing); detección de anomalías (datos financieros o de seguridad, prevención de fraudes); recomendaciones de productos (a partir de patrones de comportamiento sin etiquetas explícitas).

#### 📌 Legado y Contribución

##### Fundamentos teóricos

El PLN se apoya en fundamentos teóricos de la lingüística, la estadística y la informática que permitieron crear algoritmos para comprender y generar lenguaje.

**Lingüística.** Aporta el marco teórico esencial:
1. **Fonología**: estudia los sonidos del lenguaje, base del reconocimiento de voz y la síntesis de texto a voz.
2. **Sintaxis**: estructura gramatical de las oraciones; la gramática generativa de Noam Chomsky influyó en modelos sintácticos.
3. **Semántica**: significado de palabras y oraciones; la semántica formal llevó a representaciones semánticas.
4. **Pragmática**: uso del lenguaje en contextos específicos; guio sistemas que entienden contexto e intención.

**Modelos estadísticos.** Posibilitados por grandes volúmenes de datos y mayor capacidad computacional:
1. **N-gramas**: probabilidad de que una palabra siga a otra, base de la corrección ortográfica y la predicción de texto.
2. **Modelos de Markov**: modelan secuencias de eventos; los modelos ocultos de Markov (HMM) son útiles en el etiquetado de partes del discurso.
3. **Vectorización y espacios vectoriales**: palabras como vectores multidimensionales que capturan relaciones semánticas y sintácticas (similitud de documentos, clasificación de texto).

**Aprendizaje automático y redes neuronales.** Permiten aprender de los datos sin programación explícita:
1. **ANN**: imitan la estructura del cerebro y aprenden patrones complejos.
2. **CNN**: usadas en imágenes y también en análisis de texto (clasificación de sentimientos).
3. **RNN**: útiles para secuencias, ya que mantienen información de estados anteriores (traducción automática).

##### Inspiración para investigación futura

Los modelos pioneros motivaron mejoras en arquitecturas y algoritmos:

**Representaciones semánticas.**
- **Word Embeddings**: Word2Vec y GloVe captan relaciones semánticas complejas, mejorando traducción automática y análisis de sentimientos.
- **Contextualización**: ELMo y BERT consideran el contexto de la palabra, con representaciones más precisas; la investigación futura podría integrar múltiples capas de contexto.

**Transformadores y aprendizaje profundo.**
- **Arquitecturas de transformadores**: manejan dependencias a largo plazo y procesamiento paralelo, base de modelos como GPT-3 y T5.
- **Aprendizaje auto-supervisado**: aprende de grandes cantidades de datos no etiquetados, dando modelos más robustos y generalizables.

**Multimodalidad.** La integración de texto con imágenes y sonido gana atención; modelos como CLIP y DALL-E muestran que la información multimodal enriquece la comprensión semántica.

**Ética y responsabilidad.**
- **Sesgos en modelos de lenguaje**: necesidad de identificar y mitigar los sesgos de los datos de entrenamiento para sistemas justos.
- **Transparencia y explicabilidad**: la opacidad del aprendizaje profundo plantea desafíos de confianza; las técnicas de explicabilidad son cruciales.

### 👾 Conclusión

<p align="center"><img src="assets/img/1990-d.png" alt="Ilustración" width="460"></p>


<p align="center"><img src="assets/img/1990-c.png" alt="Ilustración" width="460"></p>


La década de 1990 consolidó las redes neuronales y las representaciones distribuidas como base del PLN moderno. La popularización de la retropropagación (Werbos 1974; Rumelhart, Hinton y Williams 1986), los modelos conexistas y arquitecturas pioneras como las redes de Hopfield (1982) y las redes recurrentes de Elman (1990) y Jordan sentaron los fundamentos teóricos del aprendizaje profundo. Sus aplicaciones en modelado del lenguaje y desambiguación lexical convivieron con limitaciones serias: alto coste computacional, predominio de métodos supervisados y el problema del vanishing gradient. Estas limitaciones, superadas en parte por LSTM, GRU, Word2Vec, los embeddings contextuales (ELMo, BERT, GPT) y los Transformers, junto con los avances en aprendizaje no supervisado, multimodalidad y ética, confirman a esta etapa como punto de partida imprescindible de la evolución posterior del procesamiento del lenguaje natural.

> [!TIP] 😄 Pausa
> Las redes de los 90 sufrían el *vanishing gradient*: la motivación se desvanece capa tras capa. Relatable.

## 🏠 Primeros 2000: Modelos Probabilísticos y Topic Modeling

<p align="center"><img src="assets/img/2000-a.png" alt="Ilustración" width="460"></p>


### 👾 Introducción de Modelos como Latent Dirichlet Allocation (LDA)

> [!TIP] 😄 Pausa
> Un "tópico" en LDA es una distribución de palabras. Mi tópico favorito es una distribución de siestas.


#### 📌 1. Evolución del Topic Modeling

##### Pritchard et al. (2000): Introducción de modelos genéticos que influyeron en LDA

La obra de Pritchard et al. (2000) fue fundamental en el desarrollo de modelos genéticos que influyeron en diversas áreas, incluido el procesamiento de lenguaje natural (PLN) y, en particular, la modelización de temas mediante Latent Dirichlet Allocation (LDA). Sus conceptos de genética y evolución se aplican a la inferencia estadística y al aprendizaje automático.

Los modelos genéticos son herramientas matemáticas que representan la variabilidad genética en poblaciones. Pritchard y sus coautores introdujeron un enfoque bayesiano para inferir la estructura poblacional a partir de datos genéticos, modelando las poblaciones como mezclas de subpoblaciones, cada una con una distribución particular de genotipos.

LDA es un modelo generativo que descubre temas en colecciones de documentos. Asume que cada documento es una mezcla de temas y que cada tema es una distribución de palabras, infiriendo las distribuciones subyacentes a partir de los datos observados.

La conexión entre ambos modelos radica en cómo abordan la mezcla y la inferencia:

1. **Inferencia bayesiana**: ambos usan técnicas bayesianas para inferir las distribuciones subyacentes. En LDA se emplea el muestreo de Gibbs, similar a los enfoques de Pritchard para inferir la estructura poblacional.
2. **Modelos de mezcla**: en Pritchard et al. las poblaciones son mezclas de subpoblaciones; en LDA los documentos son mezclas de temas, cada uno con su distribución de palabras.
3. **Distribución de Dirichlet**: Pritchard et al. introdujeron su uso, componente crucial también en LDA, que captura la variabilidad en el número de temas y su representación en los documentos.

Estos modelos permitieron una mayor comprensión de la inferencia en contextos complejos e influyeron en el desarrollo de técnicas de PLN. La intersección de genética y PLN resalta la importancia de los enfoques interdisciplinarios en el análisis de datos.

##### Blei, Ng y Jordan (2003): Proponen LDA como modelo generativo

#### 📌 2. Fundamentos de LDA

##### Modelo Generativo: los documentos son mezcla de temas, y los temas son distribuciones de palabras

Los modelos generativos son modelos estadísticos que explican cómo se generan los datos. En PLN son útiles para el análisis de texto y la representación semántica, ya que capturan la estructura subyacente de los documentos: asumen que los documentos son mezclas de temas y que cada tema es una distribución de palabras.

###### Documentos como mezcla de temas

Cada documento se considera una mezcla de varios temas. Por ejemplo, un artículo de noticias puede contener política, deportes y economía, con proporciones variables. El modelo formaliza esto asignando probabilidades a los temas de cada documento.

###### Temas como distribuciones de palabras

Cada tema se modela como una distribución de palabras: se asocia una probabilidad a cada palabra del vocabulario. En un tema de "salud", palabras como "medicina", "enfermedad" y "tratamiento" tendrían alta probabilidad, mientras que "deporte" o "tecnología" tendrían probabilidad baja.

###### Proceso generativo

1. **Selección de temas**: se selecciona una mezcla de temas mediante un vector de proporciones que indica cuánto de cada tema hay en el documento.
2. **Generación de palabras**: para cada palabra se elige un tema según esa mezcla y luego una palabra de la distribución de palabras de ese tema.
3. **Iteración**: se repite hasta generar el número deseado de palabras.

Idea central del modelo generativo:

```
P(palabra | documento) = Σ_tópico  P(palabra | tópico) · P(tópico | documento)
```

###### Componentes de LDA

- **Parámetros de Dirichlet**: LDA usa distribuciones de Dirichlet para modelar la mezcla de temas en documentos y la mezcla de palabras en temas, controlando su diversidad.
- **Inferencia**: estima las distribuciones de temas y palabras mediante técnicas como el muestreo de Gibbs o la inferencia variacional (variational inference).

###### Aplicaciones de modelos generativos

- **Agrupamiento de documentos** similares según sus temas.
- **Recomendaciones de contenido** según los temas de interés del usuario.
- **Análisis de sentimientos**, identificando temas subyacentes en opiniones o reseñas.

##### Dirichlet Distribution: distribución usada para modelar las distribuciones de temas y palabras

La distribución de Dirichlet es fundamental en el modelado de temas y palabras dentro del PLN, especialmente en modelos generativos.

###### Definición y propiedades

Es una distribución continua en el espacio de probabilidad de K dimensiones, donde K es el número de categorías o temas:

```
p(x) = (1 / B(α)) · Π_{k=1..K}  x_k^(α_k − 1)

donde:
  x = (x_1, ..., x_K)   proporciones de cada categoría, con x_k ≥ 0 y Σ_{k=1..K} x_k = 1
  α = (α_1, ..., α_K)   vector de parámetros que determina la forma
  B(α)                  función beta multivariada (factor de normalización)
```

Los parámetros α = (α_1, ..., α_K) se interpretan como "pseudo-contadores" del número esperado de apariciones de cada categoría:

- Si todos los α_k son iguales y mayores que 1, la distribución es más uniforme.
- Si algunos α_k son menores que 1, se concentra en ciertas categorías.

Propiedades clave:

1. **Suma a uno**: Σ x_k = 1, lo que permite interpretarlas como probabilidades.
2. **Concentración**: valores altos de α dan una distribución concentrada en torno a la media; valores bajos permiten más variabilidad.
3. **Conexión con la distribución beta**: la Dirichlet es una generalización de la beta; con K = 2 se reduce a la beta, usada para modelar proporciones.

###### Aplicaciones en PLN

En LDA, la Dirichlet modela tanto la distribución de temas en un documento como la distribución de palabras en un tema:

1. **Distribución de temas por documento**: cada documento es una Dirichlet sobre el conjunto de temas, con una mezcla única.
2. **Distribución de palabras por tema**: cada tema es una Dirichlet sobre el vocabulario, con su propio estilo y léxico.

Su capacidad para manejar proporciones y su flexibilidad paramétrica la hacen idónea para representar la complejidad del lenguaje.

#### 📌 3. Proceso de LDA

##### Asignación de Temas a Palabras: cada palabra de un documento se asigna a un tema

La asignación de temas a palabras identifica y categoriza el contenido semántico de un documento, organizando la información y facilitando la recuperación de datos y el análisis semántico.

###### Conceptos clave

1. **Tema**: conjunto de palabras con significado o contexto común, representado como distribución de palabras frecuentes en contextos similares.
2. **Palabra**: unidad básica de análisis; puede asignarse a uno o más temas según su contexto.
3. **Modelo de asignación de temas**: algoritmos que identifican patrones y asignan cada palabra a temas. Ejemplos: LDA (Latent Dirichlet Allocation) y NMF (Non-negative Matrix Factorization).

###### Proceso de asignación

1. **Preprocesamiento de texto**:
   - **Tokenización**: dividir el texto en palabras.
   - **Normalización**: minúsculas y eliminación de puntuación.
   - **Eliminación de palabras vacías**: filtrar palabras sin significado ("y", "el", "de").
2. **Representación de documentos**:
   - **Matriz de términos**: filas = documentos, columnas = palabras; cada celda contiene la frecuencia de una palabra en un documento.
3. **Aplicación del modelo**: identificar la distribución de palabras y asignar temas. En LDA, cada documento es una mezcla de temas y cada tema una mezcla de palabras.
4. **Interpretación de resultados**: analizar los temas y palabras asociadas para interpretar su significado y relevancia.

###### Métodos comunes

1. **Latent Dirichlet Allocation (LDA)**: cada documento es combinación de temas y cada tema combinación de palabras; usa un enfoque probabilístico para inferir la distribución de temas.
2. **Non-negative Matrix Factorization (NMF)**: descompone la matriz de términos en dos matrices menores (temas y su distribución en documentos). No asume una Dirichlet y es más adecuado para datos no negativos.
3. **Modelos basados en redes neuronales**: autoencoders y redes convolucionales capturan relaciones más complejas entre palabras y temas.

###### Aplicaciones

- **Organización de contenidos**: clasificar grandes volúmenes de texto (artículos, libros, redes sociales).
- **Análisis de sentimiento**: identificar temas relevantes en opiniones.
- **Recomendación de contenidos**: entender intereses temáticos de los usuarios.
- **Resumen automático**: identificar los temas más relevantes de un documento.

###### Desafíos

- **Ambigüedad semántica**: una palabra puede tener múltiples significados según el contexto.
- **Escalabilidad**: procesar grandes volúmenes exige algoritmos eficientes.
- **Interpretabilidad**: los resultados suelen ser difíciles de interpretar.

##### Inferencia de Temas: métodos como Gibbs Sampling para estimar distribuciones

La inferencia de temas descubre la estructura latente en grandes colecciones de textos, identificando temas que agrupan palabras y documentos de forma coherente. Uno de los métodos más usados es el muestreo de Gibbs, dentro de los modelos de tópicos.

Los modelos de tópicos como LDA asumen que cada documento es mezcla de temas y que cada tema se caracteriza por una distribución de palabras. Componentes clave:

1. **Documentos**: conjuntos de palabras que representan información textual.
2. **Temas**: conjuntos de palabras agrupadas por su coocurrencia.
3. **Distribuciones**: de probabilidad, entre documentos-temas y temas-palabras.

###### Muestreo de Gibbs

Método de muestreo estadístico para estimar distribuciones de probabilidad complejas. En la inferencia de temas se usa para inferir las variables latentes (asignaciones de temas a palabras y documentos).

Proceso:

1. **Inicialización**: se asignan aleatoriamente temas a cada palabra del corpus, de forma uniforme o heurística.
2. **Iteración**: para cada palabra de cada documento se calcula la probabilidad de que pertenezca a cada tema (dado el contexto y las asignaciones actuales) y se le asigna un tema en función de esas probabilidades.
3. **Convergencia**: se repite durante un número de iteraciones o hasta que las asignaciones se estabilicen.

El cálculo de probabilidades se basa en la regla de Bayes, considerando la proporción de palabras del documento ya asignadas a ese tema y la proporción de palabras del corpus asociadas a ese tema:

```
P(z_i = k | z_{-i}, w)  ∝  ( (n_dk + α) / (n_d + K·α) ) · ( (n_kw + β) / (n_k + V·β) )

donde:
  z_i   asignación de tema para la palabra i
  n_dk  nº de palabras del documento d asignadas al tema k
  n_kw  nº de veces que la palabra w fue asignada al tema k
  n_d   total de palabras en el documento d
  n_k   total de palabras asignadas al tema k
  V     vocabulario total
  α, β  hiperparámetros que controlan las distribuciones de temas y palabras
```

Ventajas: **simplicidad** (fácil de implementar y entender) y **flexibilidad** (se adapta a distintos modelos y distribuciones).

Desventajas: **convergencia lenta** (muchas iteraciones) y **dependencia de la inicialización**.

### 👾 Cómo los Modelos Probabilísticos Influyeron en la Semántica Vectorial

<p align="center"><img src="assets/img/2000-b.png" alt="Ilustración" width="460"></p>


#### 📌 1. Representación Probabilística del Lenguaje

##### Captura de Incertidumbre: palabras y temas con distribuciones de probabilidad asociadas

La captura de incertidumbre modela la variabilidad inherente del lenguaje. Como palabras y temas pueden interpretarse de varias maneras, se representan mediante distribuciones de probabilidad, lo que permite manejar la ambigüedad.

Cada palabra puede asociarse a una distribución que refleja su probabilidad de ocurrencia en distintos contextos. Por ejemplo, "banco" puede ser institución financiera o asiento, según el contexto:

- "banco" como institución financiera: 70%
- "banco" como asiento: 20%
- "banco" en otros contextos: 10%

Los temas también se modelan con distribuciones. En un corpus de deportes y tecnología:

- Tema 1 (Deportes): "fútbol" 40%, "baloncesto" 30%, "tenis" 30%
- Tema 2 (Tecnología): "inteligencia artificial" 50%, "computación cuántica" 30%, "robótica" 20%

Estos temas permiten clasificar documentos y entender la estructura semántica del corpus.

###### Técnicas para capturar incertidumbre

1. **Modelos de lenguaje basados en n-gramas**: usan la frecuencia de secuencias de palabras para estimar la probabilidad de una palabra dado su contexto.
2. **Word embeddings**: representaciones vectoriales como Word2Vec y GloVe que capturan relaciones semánticas y distribuciones de contexto.
3. **Modelos basados en atención**: redes neuronales que ponderan la importancia de cada palabra de una oración.
4. **Inferencia bayesiana (Bayesian inference)**: actualiza las creencias sobre la probabilidad de un evento al obtener nueva información.

##### Flexibilidad: manejo probabilístico de polisemia y sinónimos

La flexibilidad es la capacidad de manejar la polisemia y los sinónimos de manera probabilística, fundamental para comprender y generar lenguaje.

###### Polisemia

Fenómeno por el que una palabra tiene múltiples significados. "Banco" puede ser institución financiera u objeto para sentarse; el significado depende del contexto. En "El banco estaba lleno de gente" se refiere a la institución; en "Me senté en el banco del parque", al asiento.

###### Sinónimos

Palabras con significados similares o idénticos, como "feliz" y "contento". Su uso varía según el contexto: "Ella estaba feliz con su regalo" puede transmitir un sentimiento más intenso que "Ella estaba contenta con su regalo". El sistema debe elegir el sinónimo adecuado para mantener la precisión semántica.

###### Manejo probabilístico

Se logra con enfoques probabilísticos que infieren a partir de datos mediante técnicas estadísticas y de aprendizaje automático. Modelos de lenguaje como **Word2Vec**, **GloVe** y **BERT** emplean representaciones vectoriales:

- **Word2Vec**: aprende representaciones semánticas mediante el contexto de palabras; cada palabra es un vector en un espacio multidimensional donde las de significado similar están más cerca.
- **BERT**: introduce el concepto de "atención" y considera el contexto completo de la palabra en la oración, muy efectivo para la polisemia.

Consideraciones: el **contexto** es crucial para desambiguar; la calidad y diversidad de los **datos de entrenamiento** son vitales; y la **interpretabilidad** se dificulta a medida que los modelos se vuelven más complejos.

#### 📌 2. Ventajas sobre Modelos Determinísticos

##### Escalabilidad: manejo eficiente de grandes corpus

La escalabilidad es la capacidad de manejar un aumento de la carga, ya sea ampliando recursos (escalabilidad vertical) o distribuyéndola entre varios recursos (escalabilidad horizontal). En PLN implica procesar, almacenar y analizar grandes cantidades de texto con eficiencia.

Desafíos con grandes corpus:

1. **Almacenamiento**: requieren soluciones rápidas y multiformato. Las bases NoSQL como MongoDB y Elasticsearch son frecuentes por su flexibilidad y escalado horizontal.
2. **Procesamiento**: exige algoritmos eficientes en tiempo y espacio, con técnicas por lotes o en tiempo real.
3. **Análisis**: requiere algoritmos escalables y modelos de aprendizaje automático entrenables en datos masivos sin perder calidad.

Estrategias:

1. **Sistemas distribuidos**: Apache Hadoop y Apache Spark dividen el procesamiento entre múltiples nodos.
2. **Procesamiento por lotes**: acumular y procesar datos en conjunto (tokenización, etiquetado, extracción de características).
3. **Optimización de algoritmos**: muestreo, reducción de dimensionalidad y paralelización.
4. **Almacenamiento eficiente**: formatos como Parquet o Avro y técnicas de compresión.

Herramientas: **Apache Hadoop** (procesamiento distribuido en clústeres), **Apache Spark** (programación de clústeres orientada a velocidad y facilidad), **Elasticsearch** (búsqueda y análisis en tiempo real) y **Dask** (computación paralela en Python).

##### Actualización Incremental: incorporar nuevos datos sin reconstruir el modelo completo

Permite añadir nuevos datos a un modelo existente sin reconstruirlo desde cero. Es valiosa cuando los datos son dinámicos (minería de textos, análisis de sentimientos, sistemas de recomendación).

Importancia:

1. **Eficiencia computacional**: ajusta solo los parámetros necesarios, reduciendo tiempo y recursos.
2. **Adaptabilidad**: mantiene el modelo relevante ante nuevas tendencias (redes sociales, comercio electrónico).
3. **Minimización de la pérdida de información**: preserva las características aprendidas previamente.

Métodos:

1. **Ajuste de parámetros**: modificar solo los parámetros afectados (pesos en regresión o redes neuronales).
2. **Algoritmos basados en ejemplos**: aprendizaje por refuerzo o en línea, que se adaptan a nuevas entradas sin acceder a todo el conjunto previo.
3. **Modelos de memoria**: redes como LSTM almacenan información relevante y se actualizan eficientemente.

Desafíos:

1. **Desviación de concepto (drift)**: los patrones cambian con el tiempo y el modelo puede quedar obsoleto.
2. **Manejo de ruido**: los nuevos datos pueden introducir ruido; se requieren filtrado y validación.
3. **Complejidad de implementación**: exige una arquitectura más compleja que el entrenamiento tradicional.

#### 📌 3. Aplicaciones Prácticas

##### Análisis de Sentimiento: detección de emociones y opiniones en textos

Subdisciplina del PLN que identifica y extrae opiniones y emociones de un texto. Ha cobrado relevancia por el crecimiento de datos generados por usuarios (redes sociales, reseñas, foros), permitiendo decisiones informadas basadas en la percepción del público.

Tipos:

1. **A nivel de documento**: evalúa el sentimiento general del texto (positivo, negativo o neutral).
2. **A nivel de oración**: analiza cada oración por separado, captando sentimientos contradictorios.
3. **A nivel de aspecto**: identifica sentimientos sobre aspectos específicos; p. ej., en una reseña de restaurante, separa comida, servicio y ambiente.

Técnicas:

- **Enfoques basados en reglas**: usan diccionarios o léxicos de sentimientos ("excelente" positivo, "terrible" negativo). Sencillos, pero dependen de la exhaustividad del léxico y no manejan bien el contexto.
- **Enfoques basados en aprendizaje automático**: entrenados con datos etiquetados. Algoritmos comunes: **Regresión Logística**, **Máquinas de Vectores de Soporte (SVM)** y **Redes Neuronales**.
- **Enfoques basados en aprendizaje profundo**: modelos como **LSTM** (Long Short-Term Memory) y **Transformers** como BERT (Bidirectional Encoder Representations from Transformers), efectivos por considerar el contexto de las palabras.

Desafíos:

1. **Ironía y sarcasmo**: las palabras pueden significar lo opuesto a lo esperado.
2. **Ambigüedad lingüística**: una palabra puede tener varios significados según el contexto (p. ej., "banco").
3. **Contexto cultural y lingüístico**: las expresiones varían entre culturas e idiomas.

Aplicaciones:

- **Análisis de reseñas de productos**: evaluar la percepción de consumidores.
- **Monitoreo de redes sociales**: rastrear la opinión pública sobre eventos o campañas.
- **Atención al cliente**: identificar problemas y mejorar la satisfacción.

##### Recomendación de Contenidos: sugerencias según temas de interés del usuario

Área del PLN y la IA que ofrece sugerencias personalizadas según intereses y comportamientos previos del usuario, cada vez más necesaria ante el crecimiento exponencial de información en línea.

Tipos de sistemas:

1. **Basados en contenidos**: analizan las características de los elementos y las comparan con las preferencias del usuario, usando PLN para extraer características semánticas. *Ejemplo*: recomendar libros por género, autor y temas leídos previamente.
2. **Colaborativos**: usan las interacciones de múltiples usuarios, identificando patrones y gustos comunes. *Ejemplo*: sugerir películas según lo que vieron y valoraron usuarios con gustos similares.
3. **Híbridos**: combinan ambos enfoques para mayor precisión. *Ejemplo*: un servicio de streaming que usa el historial del usuario y las valoraciones de otros.

Técnicas de PLN:

- **Análisis de sentimiento**: entiende opiniones y emociones de comentarios o reseñas.
- **Extracción de temas**: algoritmos como LDA (Latent Dirichlet Allocation) identifican temas recurrentes para categorizar y recomendar.
- **Modelado de lenguaje**: word embeddings como Word2Vec o GloVe capturan relaciones semánticas y facilitan la comparación de contenido.

Métricas de evaluación: **precisión** (proporción de recomendaciones relevantes), **cobertura** (ítems únicos recomendables), **diversidad** (variedad de recomendaciones) y **satisfacción del usuario** (encuestas o feedback).

Desafíos: **escalabilidad** ante más usuarios y elementos, **frío inicial (cold start)** con nuevos usuarios o elementos sin datos históricos, y **cambios en el comportamiento del usuario** que exigen sistemas dinámicos.

#### 📌 4. Limitaciones

##### Número de Temas: necesidad de predefinir la cantidad de temas

La predefinición del número de temas influye en la calidad y relevancia de los resultados en tareas como clasificación de texto, análisis de sentimientos y generación de resúmenes.

1. **Claridad y enfoque**: un número específico de temas establece un marco claro y facilita identificar patrones y relaciones.
2. **Precisión del modelo**: demasiados temas pueden causar sobreajuste (el modelo memoriza en vez de generalizar); muy pocos pierden información relevante. Es clave equilibrar.
3. **Interpretación de resultados**: temas bien definidos facilitan comprender las conclusiones, importante para tomadores de decisiones (p. ej., opiniones en redes sociales).
4. **Optimización de recursos**: limitar los temas reduce la complejidad del modelo, el tiempo de entrenamiento y la carga computacional.
5. **Análisis comparativo**: un marco común permite evaluar distintos enfoques bajo las mismas condiciones, mejorando la validez de las conclusiones.
6. **Selección de temas**: hay que considerar la naturaleza del corpus, los objetivos del análisis, las características del modelo y las técnicas de agrupamiento y clasificación.

##### Interpretabilidad: dificultad para asignar significado concreto a los temas descubiertos

La interpretabilidad es la capacidad de entender y explicar cómo y por qué un modelo toma decisiones, especialmente relevante en modelos complejos como las redes neuronales profundas, cuyos patrones suelen ser opacos.

Importancia:

- **Confianza del usuario**: necesaria en aplicaciones sensibles (medicina, justicia).
- **Diagnóstico de errores**: comprender las conclusiones permite identificar y corregir errores o sesgos.
- **Cumplimiento normativo**: muchas jurisdicciones exigen decisiones automatizadas explicables (banca, atención médica).

Desafíos:

- **Complejidad de los modelos**: los basados en transformadores (BERT, GPT) suelen ser "cajas negras".
- **Representaciones semánticas**: los vectores capturan relaciones semánticas, pero son difíciles de traducir a conceptos humanos concretos.
- **Ambigüedad del lenguaje**: el significado de los patrones varía según el contexto.

Métodos de mejora:

- **Visualización**: t-SNE o PCA para visualizar representaciones de alta dimensión.
- **Modelos más simples**: regresiones lineales o árboles de decisión, más interpretables aunque con menor rendimiento.
- **Técnicas de explicación**: LIME (Local Interpretable Model-agnostic Explanations) y SHAP (SHapley Additive exPlanations) destacan qué características fueron más importantes en una predicción.

Aplicaciones: **análisis de sentimientos** (entender clasificaciones para ajustar marketing), **chatbots y asistentes virtuales** (explicar respuestas mejora la satisfacción) y **detección de sesgos** (identificar y mitigar sesgos para un uso más ético).

### 👾 Conclusión

<p align="center"><img src="assets/img/2000-d.png" alt="Ilustración" width="460"></p>


<p align="center"><img src="assets/img/2000-c.png" alt="Ilustración" width="460"></p>


Los modelos probabilísticos de los primeros 2000 sentaron las bases del topic modeling moderno. Desde los modelos genéticos de Pritchard et al. (2000) hasta la formulación de LDA por Blei, Ng y Jordan (2003), la inferencia bayesiana y la distribución de Dirichlet ofrecieron un marco generativo para representar documentos como mezclas de temas y temas como distribuciones de palabras. Estos enfoques aportaron captura de incertidumbre, flexibilidad ante la polisemia y los sinónimos, escalabilidad y actualización incremental frente a los modelos determinísticos, e impulsaron aplicaciones como el análisis de sentimiento y la recomendación de contenidos. Sus limitaciones —la necesidad de predefinir el número de temas y la dificultad de interpretación— siguen siendo retos abiertos, y la intersección interdisciplinaria que originó LDA continúa guiando el desarrollo de modelos más sofisticados de PLN.

> [!TIP] 😄 Pausa
> LDA asume que cada documento es una mezcla de tópicos. Este: 60% historia, 30% álgebra, 10% chistes malos.
