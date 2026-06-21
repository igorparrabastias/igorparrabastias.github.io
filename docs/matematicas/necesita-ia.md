# Lo que de verdad necesita la IA

Existe un mito persistente: que la inteligencia artificial es, sobre todo, **cálculo** (derivadas e integrales). El cálculo aparece —en el entrenamiento, vía el descenso de gradiente— pero no es el cimiento. La IA moderna se sostiene sobre **cuatro patas**, y si falta una, la mesa se cae: **álgebra lineal, estadística y probabilidad, datos y poder de cómputo**. El hilo histórico de cómo se fueron ensamblando está en la serie [Fundamentos del PLN y la IA](../fundamento-del-pln-y-la-ia.md).

## Álgebra lineal

Es **la lengua materna de la IA**. Por dentro, un modelo no manipula palabras ni píxeles, sino **vectores, matrices y tensores** (tablas de números de varias dimensiones). Una palabra se representa como un *embedding* —un vector de cientos o miles de números— y casi todo lo que hace una red neuronal al procesarla se reduce a **multiplicaciones de matrices** seguidas de una función no lineal, capa tras capa. El "significado" se vuelve geometría: conceptos parecidos quedan **cerca** en el espacio vectorial, y la **similitud del coseno** (el ángulo entre dos vectores) mide ese parecido. Operaciones como la analogía *rey − hombre + mujer ≈ reina* son, literalmente, aritmética de vectores.

Esto explica además **por qué la IA corre en GPUs**: una tarjeta gráfica es, en esencia, una máquina de multiplicar matrices enormes en paralelo, justo lo que un modelo necesita millones de veces. Y técnicas de reducción como **PCA** y **SVD** —descomponer una matriz en sus direcciones principales— son álgebra lineal pura, y fueron clave para los primeros métodos semánticos. El detalle histórico está en [Orígenes (PCA, espacios vectoriales)](../fundamentos-1-origenes.md) y en [Estadística y redes (SVD/LSA)](../fundamentos-2-estadistica-redes.md).

## Estadística y probabilidad

Si el álgebra lineal es *cómo* se mueven los números, la estadística es *cómo se decide bajo incertidumbre*. Un modelo de IA casi nunca afirma con certeza: estima **probabilidades**. Un LLM, de hecho, no hace otra cosa que modelar la distribución *P(siguiente token | contexto)* y muestrear de ella; la capa final **softmax** convierte sus números internos en una distribución de probabilidad sobre el vocabulario. Un clasificador de imágenes no dice "es un gato", dice "gato con probabilidad 0,95".

De aquí salen los conceptos que de verdad importan al construir modelos: **verosimilitud** y estimación por máxima verosimilitud (el objetivo que se optimiza al entrenar), el compromiso **sesgo–varianza** y el **sobreajuste** (memorizar en vez de generalizar), y las métricas honestas de evaluación —**precisión, exhaustividad (*recall*)**, F1— que evitan engañarse con la mera exactitud. El pensamiento **bayesiano** —actualizar creencias con la evidencia— recorre todo el campo. Para profundizar: el notebook [Probabilidad y Estadística en Algoritmos](../notebook/transicion-a-experto-matematicas-y-teoria-detras-de-los-algoritmos/probabilidad-y-estadistica-en-algoritmos.ipynb) (en [Teoría detrás de los algoritmos](teoria.md)), y los [modelos probabilísticos y de tópicos (LDA)](../fundamentos-2-estadistica-redes.md) en la serie.

## Datos (big data)

Ningún algoritmo brillante compensa unos datos malos: **los datos son el combustible**. Un modelo aprende los patrones que están en sus datos —y también sus sesgos y errores—, así que **la calidad y la diversidad importan tanto o más que la cantidad**. Detrás de cada modelo hay un *pipeline* poco glamoroso pero decisivo: **recolección, limpieza, deduplicación, etiquetado y curación**, además de decisiones de **almacenamiento y formato** para mover terabytes o petabytes sin morir en el intento.

A escala web, esto se vuelve un problema de ingeniería en sí mismo, y tiene un límite real: el **"muro de los datos"** (el texto de alta calidad es finito), que empuja hacia los **datos sintéticos** y la curación fina —lo trato en [Investigación reciente y futuro](../fundamentos-4-investigacion-futuro.md)—. En el lado aplicado, las **bases de datos vectoriales** permiten buscar por significado y son el corazón de los sistemas **RAG** (ver [IA práctica](../ia-practica/index.md)). Una buena puerta de entrada al oficio del dato es [Data Ecosystem (IBM)](../practica/ibm-data-ecosystem.md).

## Cómputo (cloud computing)

La cuarta pata es **el músculo**: sin un poder de cálculo enorme, las otras tres no se mueven. Entrenar un modelo grande exige **miles de GPUs o TPUs** trabajando en paralelo durante semanas, coordinadas con técnicas de **entrenamiento distribuido** (repartir el modelo y los datos entre muchas máquinas). Eso vive, casi siempre, en la **nube** (GCP, AWS y similares), que ofrece ese hardware bajo demanda y permite **escalar** hacia arriba para entrenar y hacia los lados para **servir** el modelo a millones de usuarios.

Y aquí el coste deja de ser una abstracción: la factura ya no se mide solo en dinero, sino en **gigavatios de electricidad y litros de agua** de refrigeración. La cara física de todo esto —megaclusters, energía, agua e incluso datacenters en el espacio— la desarrollo en [Infraestructura y costos](../fundamentos-4-investigacion-futuro.md). Saber repartir el cálculo y elegir bien los servicios en la nube es hoy una competencia tan central como el propio modelo.

> [!NOTE]
> Resumen: **cálculo** ayuda a *entrenar* (gradientes), pero las cuatro patas que *sostienen* la IA son **álgebra lineal** (representar y combinar), **estadística** (decidir con incertidumbre), **datos** (de qué aprende) y **cómputo** (con qué fuerza). Lo demás se construye encima.
