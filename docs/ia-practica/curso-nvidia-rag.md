# Building RAG Agents with LLMs (NVIDIA DLI) 🔵

> **Material de terceros.** Curso *Building RAG Agents with LLMs* del **NVIDIA Deep Learning Institute (DLI)**: diapositivas y código provisto. Lo estudié para profundizar en RAG de extremo a extremo, y mis propios *refactors* y ejercicios viven en el subdirectorio `course/practice/`. Es el complemento "industrial" a mis proyectos propios de [RAG](rag-skyline-agent.md).

## Qué es

Un taller de NVIDIA que enseña a implementar, modularizar y **evaluar** un agente RAG capaz de responder preguntas sobre una colección de artículos de investigación, **sin fine-tuning**. La pila tecnológica que usa:

- **LangChain** y **LCEL** para componer cadenas.
- **NVIDIA AI Foundation Endpoints** como proveedor de modelos.
- **FAISS** como *vector store*.
- **Gradio** para la interfaz de chat.
- **LangServe** y **FastAPI** para servir el agente como microservicio.

El material original incluye una secuencia de notebooks numerados (`00_jupyterlab`, `01_microservices`, `02_llms`, `03_langchain_intro`, `04_running_state`, `05_documents`, `06_embeddings`, `07_vectorstores`, `08_evaluation`, `35_langserve`, `64_guardrails`…), las diapositivas (`DLI-RAG-Slides.pptx`) y un entorno con Docker, un *frontend* y un servidor.

> [!NOTE]
> El curso, las diapositivas y los notebooks base **son de NVIDIA DLI**, no míos. Lo que sí es trabajo propio está claramente separado en `course/practice/` (ver abajo).

## Mi práctica (trabajo propio dentro del curso)

En `course/practice/` reescribí buena parte de los notebooks como **módulos `.py` ejecutables** (más cómodos de versionar y depurar que los `.ipynb`), con un `index.py` a modo de panel de control para activar/desactivar cada experimento. Algunos ejemplos:

- `notebooks/f03_langchain_intro.py`, `f04_running_state.py`, `f05_documents.py`, `f06_embeddings.py`, `f07_vectorstores.py` — mis versiones refactorizadas de las lecciones.
- `notebooks/*_exercise.py` — los ejercicios resueltos.
- `server/` y `frontend/` — el agente servido con su interfaz.
- `db/` con índices FAISS y embeddings, y `plots/` con visualizaciones de matrices de similitud que generé para entender los embeddings.

> [!TIP]
> Convertir notebooks en `.py` y orquestarlos desde un `index.py` es mi pequeña rebelión contra el "ejecuté la celda 12 antes que la 8 y ahora nada funciona". Reproducibilidad ante todo. 🧹

## Por qué lo estudié y qué aprendí

Quería ver un RAG **completo y servido**, no solo el `prompt | llm` de juguete. Lo que me llevé:

- **El flujo RAG entero**: cargar documentos → *chunking* → embeddings → indexar en FAISS → recuperar → aumentar el prompt → generar.
- **Estado conversacional** propagado por la cadena (`running_state`), idea que reutilicé en mi [RAG Skyline Agent](rag-skyline-agent.md).
- **Evaluación** de sistemas RAG: cómo medir si las respuestas realmente se apoyan en el contexto recuperado.
- **Servir el agente** como microservicio con LangServe/FastAPI y conectarlo a un frontend — el salto de "script" a "producto".

## Cómo encaja en mi sitio

Es el puente entre la teoría de la [serie PLN/IA](../fundamento-del-pln-y-la-ia.md) y mis proyectos propios: aquí está la versión "con todas las capas" (vector store real, servidor, evaluación) de las mismas ideas que practico en pequeño en [RAG de Cero a Héroe](rag-cero-a-heroe.md).

> [!QUOTE] Crédito y origen
> Curso **"Building RAG Agents with LLMs"** del **NVIDIA Deep Learning Institute (DLI)**.
>
> - Curso original (self-paced): <https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-15+V1>
> - Página del curso: <https://www.nvidia.com/en-us/training/instructor-led-workshops/building-rag-agents-with-llms/>
