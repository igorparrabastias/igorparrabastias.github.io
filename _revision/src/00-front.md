# <p align=center>**Evolución de la Representación Semántica: Fundamentos del Procesamiento del Lenguaje Natural y la IA (1950-2017)**</p>

Bienvenidos a esta serie de documentos donde exploraremos la evolución histórica del concepto de vectorizar palabras. A lo largo de las décadas, desde los años **1950 hasta el 2017**, veremos cómo han evolucionado las técnicas y teorías que nos permiten hoy en día representar palabras en forma de vectores matemáticos, fundamentales para el procesamiento del lenguaje natural y la inteligencia artificial. Esto será crucial para en una próxima serie de documentos poder entender cabalmente como funcionan los modelos más avanzados de la actualidad como son los modelos de lenguaje grandes (**LLM**) y chatbots como **ChatGPT**.

---

# :house_with_garden: **Introducción**

La evolución de la representación semántica de palabras ha sido fundamental para los avances en el procesamiento del lenguaje natural (PLN) y la inteligencia artificial (IA). Este recorrido comienza en la **década de 1950**, cuando se sentaron las bases del análisis semántico. Durante este periodo, las ideas lingüísticas iniciales comenzaron a formarse en un contexto de posguerra, con las primeras teorías que veían el lenguaje como una estructura formal y los intentos de capturar su significado mediante representaciones semánticas. Se introdujeron conceptos clave y herramientas matemáticas que influyeron en las aplicaciones tempranas, aunque con limitaciones notables.

En los **años 1960**, el trabajo de Joseph B. Kruskal y James C. Shepherd destacó por el desarrollo del análisis de escalamiento multidimensional (MDS), que permitió representar datos complejos en espacios de menor dimensión. Este enfoque se volvió relevante en lingüística, facilitando la visualización de relaciones semánticas y simplificando el análisis de grandes volúmenes de datos, aunque enfrentaba desafíos como la interpretabilidad y los altos requisitos computacionales.

La **década de 1970** trajo avances significativos con la semántica latente y el análisis de componentes principales (PCA). Aquí se profundizó en cómo los vectores podían representar relaciones semánticas en datos complejos, y el uso de técnicas estadísticas permitió comprender mejor el significado de las palabras. A pesar de las aplicaciones exitosas en lingüística y modelado estadístico, surgieron desafíos relacionados con la interpretación de los datos y la escasez de ciertos términos.

La **década de 1980** marcó el desarrollo del Análisis Semántico Latente (LSA), una técnica clave para manejar grandes volúmenes de texto mediante la descomposición en valores singulares (SVD). LSA mejoró la recuperación de información y encontró aplicaciones en educación y procesamiento del lenguaje, aunque fue criticado por sus altos costos computacionales y su dificultad para actualizarse con nuevos datos.

En los **años 1990**, las redes neuronales y las representaciones distribuidas cobraron protagonismo. Esta época vio un renacimiento de las redes neuronales, como las redes de Hopfield y las redes recurrentes de Elman y Jordan, que introdujeron nuevas formas de representar información lingüística. Sin embargo, estas técnicas enfrentaban problemas como el *vanishing gradient* y limitaciones de escalabilidad, que se compararon desfavorablemente con enfoques más recientes.

Los **primeros 2000** vieron la introducción de modelos probabilísticos y el *topic modeling*, con herramientas como Latent Dirichlet Allocation (LDA) que permitieron modelar temas en grandes corpus de texto de manera más eficiente. Estos modelos aportaron flexibilidad y capacidad de manejo de la polisemia, aunque también tenían limitaciones, como la necesidad de predefinir el número de temas y problemas de interpretabilidad.

En **2013**, la llegada de Word2Vec, desarrollado por Tomas Mikolov y su equipo de Google, simplificó y popularizó las representaciones vectoriales. Las arquitecturas de Continuous Bag of Words (CBOW) y Skip-Gram revolucionaron la forma en que se capturaban las relaciones semánticas, permitiendo operaciones aritméticas con significado lingüístico y mejorando tareas de PLN. Sin embargo, también surgieron críticas por el sesgo inherente en los datos y la limitada capacidad de manejar contextos complejos.

El **año 2017** trajo un cambio de paradigma con el modelo de transformadores, presentado en el artículo "**Attention is All You Need**". Este modelo introdujo el mecanismo de *self-attention*, que transformó el campo de PLN al mejorar la eficiencia y capturar mejor las relaciones semánticas a largo plazo. La revolución que siguió sentó las bases para modelos avanzados como BERT y GPT, que redefinieron el procesamiento de texto.

# :house_with_garden:  **Indice**

- [**Evolución de la Representación Semántica: Fundamentos del Procesamiento del Lenguaje Natural y la IA (1950-2017)**](#evolución-de-la-representación-semántica-fundamentos-del-procesamiento-del-lenguaje-natural-y-la-ia-1950-2017)
- [:house\_with\_garden: **Introducción**](#house_with_garden-introducción)
- [:house\_with\_garden:  **Indice**](#house_with_garden--indice)
- [:house\_with\_garden: **Década de 1950: Fundamentos del Análisis Semántico**](#house_with_garden-década-de-1950-fundamentos-del-análisis-semántico)
- [-- :space\_invader: **1. Contexto Histórico**](#---space_invader-1-contexto-histórico)
- [-- :space\_invader: **2. Teorías Lingüísticas Iniciales**](#---space_invader-2-teorías-lingüísticas-iniciales)
- [-- :space\_invader: **3. Primeras Representaciones Semánticas**](#---space_invader-3-primeras-representaciones-semánticas)
- [- :pager: **Principales Ideas y Bases Matemáticas de la Semántica**](#--pager-principales-ideas-y-bases-matemáticas-de-la-semántica)
- [-- :space\_invader: **1. Conceptos Clave**](#---space_invader-1-conceptos-clave)
- [-- :space\_invader: **2. Herramientas Matemáticas**](#---space_invader-2-herramientas-matemáticas)
- [-- :space\_invader: **3. Aplicaciones Tempranas**](#---space_invader-3-aplicaciones-tempranas)
- [-- :space\_invader: **4. Limitaciones y Desafíos**](#---space_invader-4-limitaciones-y-desafíos)
- [:house\_with\_garden: **Años 1960: Mapeo Multidimensional**](#house_with_garden-años-1960-mapeo-multidimensional)
- [- :pager: **Contribuciones de Joseph B. Kruskal y James C. Shepherd**](#--pager-contribuciones-de-joseph-b-kruskal-y-james-c-shepherd)
- [-- :space\_invader: **1. Introducción a los Autores**](#---space_invader-1-introducción-a-los-autores)
- [-- :space\_invader: **2. Desarrollo del Análisis Multidimensional**](#---space_invader-2-desarrollo-del-análisis-multidimensional)
- [- :pager: **Propuesta del Mapeo Multidimensional y su Relevancia**](#--pager-propuesta-del-mapeo-multidimensional-y-su-relevancia)
- [-- :space\_invader: **1. Aplicación en Lingüística**](#---space_invader-1-aplicación-en-lingüística)
- [-- :space\_invader: **2. Método del MDS**](#---space_invader-2-método-del-mds)
- [-- :space\_invader: **3. Impacto en Representaciones Vectoriales**](#---space_invader-3-impacto-en-representaciones-vectoriales)
- [-- :space\_invader: **4. Limitaciones**](#---space_invader-4-limitaciones)
- [:house\_with\_garden: **Década de 1970: Semántica Latente y Análisis de Componentes Principales**](#house_with_garden-década-de-1970-semántica-latente-y-análisis-de-componentes-principales)
- [- :pager: **Avances en la Semántica Latente y la Importancia de los Vectores en el Análisis de Datos Semánticos**](#--pager-avances-en-la-semántica-latente-y-la-importancia-de-los-vectores-en-el-análisis-de-datos-semánticos)
- [-- :space\_invader: **1. Introducción a la Semántica Latente**](#---space_invader-1-introducción-a-la-semántica-latente)
- [-- :space\_invader: **2. Análisis de Componentes Principales (PCA)**](#---space_invader-2-análisis-de-componentes-principales-pca)
- [-- :space\_invader: **3. Importancia de los Vectores**](#---space_invader-3-importancia-de-los-vectores)
- [- :pager: **Utilización de Técnicas Estadísticas para Comprender el Significado de las Palabras**](#--pager-utilización-de-técnicas-estadísticas-para-comprender-el-significado-de-las-palabras)
- [-- :space\_invader: **1. Modelado Estadístico del Lenguaje**](#---space_invader-1-modelado-estadístico-del-lenguaje)
- [-- :space\_invader: **2. Aplicaciones del PCA en Lingüística**](#---space_invader-2-aplicaciones-del-pca-en-lingüística)
- [-- :space\_invader: **3. Ejemplos Prácticos**](#---space_invader-3-ejemplos-prácticos)
- [-- :space\_invader: **4. Desafíos y Limitaciones**](#---space_invader-4-desafíos-y-limitaciones)
- [:house\_with\_garden: **Década de 1980: Latent Semantic Analysis (LSA)**](#house_with_garden-década-de-1980-latent-semantic-analysis-lsa)
- [- :pager: **Desarrollo de LSA para Representar y Analizar Grandes Volúmenes de Texto**](#--pager-desarrollo-de-lsa-para-representar-y-analizar-grandes-volúmenes-de-texto)
- [-- :space\_invader: **1. Orígenes del LSA**](#---space_invader-1-orígenes-del-lsa)
- [-- :space\_invader: **2. Fundamentos del LSA**](#---space_invader-2-fundamentos-del-lsa)
- [-- :space\_invader: **3. Proceso de LSA**](#---space_invader-3-proceso-de-lsa)
- [- :pager: **El Impacto de esta Técnica en la Comprensión Automática del Lenguaje**](#--pager-el-impacto-de-esta-técnica-en-la-comprensión-automática-del-lenguaje)
- [-- :space\_invader: **1. Mejoras en Recuperación de Información**](#---space_invader-1-mejoras-en-recuperación-de-información)
- [-- :space\_invader: **2. Aplicaciones en Educación**](#---space_invader-2-aplicaciones-en-educación)
- [-- :space\_invader: **3. Avances en Procesamiento del Lenguaje Natural**](#---space_invader-3-avances-en-procesamiento-del-lenguaje-natural)
- [-- :space\_invader: **4. Limitaciones y Críticas**](#---space_invader-4-limitaciones-y-críticas)
- [:house\_with\_garden: **Década de 1990: Redes Neuronales y Representaciones Distribuidas**](#house_with_garden-década-de-1990-redes-neuronales-y-representaciones-distribuidas)
- [- :pager: **Uso Temprano de Redes Neuronales para Representaciones Distribuidas**](#--pager-uso-temprano-de-redes-neuronales-para-representaciones-distribuidas)
- [-- :space\_invader: **1. Renacimiento de las Redes Neuronales**](#---space_invader-1-renacimiento-de-las-redes-neuronales)
- [-- :space\_invader: **2. Representaciones Distribuidas**](#---space_invader-2-representaciones-distribuidas)
- [-- :space\_invader: **3. Modelos Pioneros**](#---space_invader-3-modelos-pioneros)
- [- :pager: **Avances y Limitaciones de Estas Técnicas en Comparación con Enfoques Posteriores**](#--pager-avances-y-limitaciones-de-estas-técnicas-en-comparación-con-enfoques-posteriores)
- [-- :space\_invader: **1. Aplicaciones en Lenguaje**](#---space_invader-1-aplicaciones-en-lenguaje)
- [-- :space\_invader: **2. Limitaciones**](#---space_invader-2-limitaciones)
- [-- :space\_invader: **3. Comparación con Enfoques Posteriores**](#---space_invader-3-comparación-con-enfoques-posteriores)
- [-- :space\_invader: **4. Legado y Contribución**](#---space_invader-4-legado-y-contribución)
- [:house\_with\_garden: **Primeros 2000: Modelos Probabilísticos y Topic Modeling**](#house_with_garden-primeros-2000-modelos-probabilísticos-y-topic-modeling)
- [- :pager: **Introducción de Modelos como Latent Dirichlet Allocation (LDA)**](#--pager-introducción-de-modelos-como-latent-dirichlet-allocation-lda)
- [-- :space\_invader: **1. Evolución del Topic Modeling**](#---space_invader-1-evolución-del-topic-modeling)
- [-- :space\_invader: **2. Fundamentos de LDA**](#---space_invader-2-fundamentos-de-lda)
- [-- :space\_invader: **3. Proceso de LDA**](#---space_invader-3-proceso-de-lda)
- [- :pager: **Cómo los Modelos Probabilísticos Influyeron en la Semántica Vectorial**](#--pager-cómo-los-modelos-probabilísticos-influyeron-en-la-semántica-vectorial)
- [-- :space\_invader: **1. Representación Probabilística del Lenguaje**](#---space_invader-1-representación-probabilística-del-lenguaje)
- [-- :space\_invader: **2. Ventajas sobre Modelos Determinísticos**](#---space_invader-2-ventajas-sobre-modelos-determinísticos)
- [-- :space\_invader: **3. Aplicaciones Prácticas**](#---space_invader-3-aplicaciones-prácticas)
- [-- :space\_invader: **4. Limitaciones**](#---space_invader-4-limitaciones-1)
- [:house\_with\_garden: **Año 2013: la Revolución de Word2Vec**](#house_with_garden-año-2013-la-revolución-de-word2vec)
- [- :pager: **Propuesta de Tomas Mikolov y su Equipo de Google**](#--pager-propuesta-de-tomas-mikolov-y-su-equipo-de-google)
- [-- :space\_invader: **1. Contexto del Descubrimiento**](#---space_invader-1-contexto-del-descubrimiento)
- [-- :space\_invader: **2. Arquitecturas Clave**](#---space_invader-2-arquitecturas-clave)
- [- :pager: **Simplificación y Popularización de las Representaciones Vectoriales con el Modelo Word2Vec**](#--pager-simplificación-y-popularización-de-las-representaciones-vectoriales-con-el-modelo-word2vec)
- [-- :space\_invader: **1. Características Principales**](#---space_invader-1-características-principales)
- [-- :space\_invader: **2. Ventajas del Modelo**](#---space_invader-2-ventajas-del-modelo)
- [-- :space\_invader: **3. Impacto en Procesamiento del Lenguaje Natural**](#---space_invader-3-impacto-en-procesamiento-del-lenguaje-natural)
- [-- :space\_invader: **4. Limitaciones y Consideraciones Éticas**](#---space_invader-4-limitaciones-y-consideraciones-éticas)
- [-- :space\_invader: **5. Evolución Posterior**](#---space_invader-5-evolución-posterior)
- [:house\_with\_garden: **Año 2017: Modelo de Transformadores**](#house_with_garden-año-2017-modelo-de-transformadores)
- [-- :space\_invader: **Attention is All You Need**](#---space_invader-attention-is-all-you-need)
- [-- :space\_invader: **Revolución en NLP**](#---space_invader-revolución-en-nlp)
- [:house\_with\_garden:  **Conclusión General**](#house_with_garden--conclusión-general)

---
