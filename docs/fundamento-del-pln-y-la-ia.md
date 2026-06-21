# Evolución de la Representación Semántica: Fundamentos del Procesamiento del Lenguaje Natural y la IA (1950–presente)

Este documento recorre la evolución histórica de un problema central: **cómo representar el significado de las palabras de forma que una máquina pueda procesarlo**. Desde los años 1950 hasta los grandes modelos de lenguaje (**LLM**) actuales, veremos cómo las técnicas para convertir palabras en vectores matemáticos fueron madurando hasta hacer posibles sistemas como **ChatGPT**.

---

## Introducción

La representación semántica de palabras ha sido motor de los avances en procesamiento del lenguaje natural (PLN) e inteligencia artificial (IA). El recorrido, década a década:

- **1950** — Se sientan las bases del análisis semántico en plena posguerra: el lenguaje visto como estructura formal y los primeros intentos de capturar su significado de forma computable.
- **1960** — Kruskal y Shepard desarrollan el escalamiento multidimensional (MDS), que representa datos complejos en espacios de menor dimensión y permite visualizar relaciones semánticas.
- **1970** — Semántica latente y análisis de componentes principales (PCA): los vectores y las técnicas estadísticas empiezan a capturar el significado de las palabras.
- **1980** — El Análisis Semántico Latente (LSA), basado en la descomposición en valores singulares (SVD), gestiona grandes volúmenes de texto y mejora la recuperación de información.
- **1990** — Renacen las redes neuronales (Hopfield, redes recurrentes de Elman y Jordan) y las representaciones distribuidas, pese a problemas como el *vanishing gradient*.
- **Primeros 2000** — Modelos probabilísticos y *topic modeling* (LDA) modelan temas en grandes corpus con mayor flexibilidad.
- **2013** — Word2Vec (Mikolov, Google) populariza los *embeddings*: aritmética con significado lingüístico y un salto en las tareas de PLN.
- **2017** — Los **Transformers** ("Attention is All You Need") y el mecanismo de *self-attention* cambian el paradigma.
- **2018–hoy** — La era de los **LLM**: de los *embeddings* contextuales (BERT) a los modelos generativos a gran escala (GPT-3, ChatGPT, GPT-4, Claude), cerrando el arco que empezó en 1950.

<p align="center"><img src="assets/timeline.svg" alt="Línea de tiempo de la representación semántica, 1950 a hoy" width="700"></p>

## 📚 La serie, en 4 partes

Este recorrido está dividido en cuatro páginas; puedes leerlas en orden:

1. **[Orígenes (1950–1979)](fundamentos-1-origenes.md)** — bases lingüísticas y matemáticas del significado: MDS, PCA y semántica latente.
2. **[Estadística y redes neuronales (1980–2000s)](fundamentos-2-estadistica-redes.md)** — LSA/SVD, el renacer de las redes neuronales y el *topic modeling* (LDA).
3. **[La era de los LLM (2013–2026)](fundamentos-3-era-llm.md)** — de Word2Vec y los Transformers a cómo funcionan los LLM hoy: agentes, infraestructura y multimodalidad.
4. **[Investigación reciente y futuro próximo](fundamentos-4-investigacion-futuro.md)** — modelos de razonamiento, MoE, el debate sobre la AGI y los retos abiertos.

---
