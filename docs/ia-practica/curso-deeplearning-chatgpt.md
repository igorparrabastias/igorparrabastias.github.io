# Building Systems with the ChatGPT API (DeepLearning.AI) 🔵

> **Material de terceros.** Curso corto *Building Systems with the ChatGPT API* de **DeepLearning.AI**, impartido por **Isa Fulford (OpenAI)** y **Andrew Ng**. Conservo los notebooks de estudiante (L1, L2, L3) como apuntes. Encaja como la cara "ingeniería de aplicaciones LLM" de la serie [Fundamentos del PLN y la IA](../fundamento-del-pln-y-la-ia.md).
>
> **Curso original:** [DeepLearning.AI · Building Systems with the ChatGPT API](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/)

## Qué es

Un curso de una hora, muy práctico, sobre cómo construir **sistemas** —no solo prompts sueltos— encadenando llamadas a un LLM y haciendo que código Python interactúe con las respuestas del modelo. El hilo conductor es construir, paso a paso, un **chatbot de atención al cliente**. Los notebooks que guardo:

- **`L1_student.ipynb`** — fundamentos: tokens, formato de mensajes (roles system/user/assistant) y la mecánica de la API de chat.
- **`L2_student.ipynb`** — clasificación y **moderación** de las consultas del usuario, y evaluación de entradas por seguridad (detección de *prompt injection*).
- **`L3_student.ipynb`** — razonamiento en varios pasos con **cadena de pensamiento** (*chain-of-thought*) y *inner monologue* para tareas complejas.

> [!NOTE]
> Estos notebooks son material docente de **DeepLearning.AI / OpenAI**, no trabajo original mío. Los incluyo como apuntes de estudio.

## Por qué lo estudié

Saber llamar a un LLM es fácil; construir un **sistema fiable** alrededor es lo difícil. Este curso ataca justo eso: cómo descomponer una tarea en una **cadena de prompts**, cómo validar y moderar la entrada antes de gastar tokens, y cómo evaluar la salida. Son las disciplinas que separan un demo de un producto.

> [!TIP]
> La lección que más me marcó: el LLM es un becario brillante pero crédulo. Si no validas lo que le entra y lo que sale, hará exactamente lo que le pidan… incluso si quien lo pide es un usuario malicioso. 🛡️

## Qué aprendí

- **Encadenar prompts**: dividir un problema grande en pasos pequeños donde la salida de uno alimenta al siguiente, en lugar de pedirlo todo de una vez.
- **Moderación y seguridad**: clasificar consultas, filtrar contenido y defenderse de *prompt injection* antes de procesar.
- **Chain-of-thought e *inner monologue***: hacer que el modelo razone por pasos (y ocultar ese razonamiento al usuario final) para mejorar la calidad en tareas multi-paso.
- **Evaluación**: cómo comprobar sistemáticamente que el sistema responde bien, en vez de fiarse de "parece que funciona".

## Cómo encaja en mi sitio

Es la base de **ingeniería de prompts y sistemas** que aplico en mis proyectos propios de RAG. Las ideas de cadenas de prompts y validación de entrada/salida reaparecen, ya en código de aplicación, en el [RAG Skyline Agent](rag-skyline-agent.md) (su cadena interna que extrae y valida estado) y en el curso de [NVIDIA](curso-nvidia-rag.md). Teoría en la [serie PLN/IA](../fundamento-del-pln-y-la-ia.md); práctica aquí.

> [!QUOTE] Crédito y origen
> Curso **"Building Systems with the ChatGPT API"** de **DeepLearning.AI**, por **Isa Fulford (OpenAI)** y **Andrew Ng**.
>
> - Curso original: <https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/>
