# RAG de Cero a Héroe 🟢

> Proyecto **propio**. Un *playground* mínimo para experimentar con **LangChain** y **LlamaIndex** sobre `gpt-4o-mini`. Es el banco de pruebas donde toco las piezas básicas de un sistema RAG una a una. Complementa al [RAG Skyline Agent](rag-skyline-agent.md) (que ya es una app completa) y a la serie [Fundamentos del PLN y la IA](../fundamento-del-pln-y-la-ia.md).

## La idea

Antes de construir una catedral RAG conviene jugar con los ladrillos. Este repo es exactamente eso: un archivo `zero_to_hero.py` donde voy probando los conceptos fundamentales de LangChain — invocar un modelo, encadenar prompts, parsear salidas — con el modelo barato y rápido `gpt-4o-mini`.

> [!TIP]
> "De cero a héroe" es optimista: empezamos en "hola, ¿qué nombre le pongo a mi empresa de calcetines?" y de ahí, en teoría, se llega a Iron Man. Spoiler: el primer paso es siempre `chain.invoke(...)`. 🦸

## La configuración: una línea que lo cambia todo

La clave de OpenAI no se escribe en el código; se carga del entorno con `python-dotenv`. Todo `config.py` es esto:

```python
--8<-- "learning/courses/RAG-LangChain-LlamaIndex/config.py"
```

Importar `config` (como hace `index.py`) ejecuta `load_dotenv()` y deja la `OPENAI_API_KEY` disponible. Pequeño, pero es el patrón correcto: **secretos fuera del código**.

## Los bloques de construcción

El archivo central muestra dos formas de hablar con el modelo, que son la base de casi todo en LangChain:

```python
--8<-- "learning/courses/RAG-LangChain-LlamaIndex/course/zero_to_hero.py"
```

Desglosado, aquí están los conceptos fundacionales de cualquier sistema RAG:

1. **El modelo de chat** — `ChatOpenAI(model="gpt-4o-mini", temperature=...)`. La `temperature` controla la creatividad (0 = determinista, 0.5 = algo de chispa) y `max_tokens` acota la longitud. Es el "motor".

2. **El prompt como plantilla** — `ChatPromptTemplate.from_messages([...])` separa el rol de *system* (instrucciones permanentes: *"eres un asistente de nombres de empresa"*) del *human* (la pregunta, con variables como `{product}`). Esto es lo que luego, en un RAG real, rellenas con el **contexto recuperado**.

3. **La cadena (LCEL)** — el operador pipe: `chain = prompt | llm`. LangChain Expression Language deja **componer** piezas como tuberías de Unix. Le sumas un `StrOutputParser()` y la salida deja de ser un objeto `Message` para ser texto plano, listo para mostrar.

4. **La invocación** — `chain.invoke({"product": "..."})` ejecuta toda la tubería con los valores concretos.

### ¿Y dónde está el "RAG"?

Estos cuatro bloques son la mitad del patrón: *aumentar el prompt → generar*. Lo que falta —y es lo que se explora en los proyectos hermanos— es la otra mitad:

- **Indexación**: trocear documentos (*chunking*), calcular **embeddings** y guardarlos en un *vector store* (FAISS, Chroma…). Aquí entra **LlamaIndex**, especializado justo en esa capa de ingestión y consulta.
- **Recuperación**: dado el mensaje del usuario, buscar los *chunks* más parecidos por similitud vectorial y meterlos en el `{context}` del prompt.

Una vez tienes el reflejo `prompt | llm | parser`, añadir un *retriever* delante (`retriever | prompt | llm`) es un paso natural — y es precisamente lo que ya hace el [RAG Skyline Agent](rag-skyline-agent.md) con su cadena interna/externa.

## Qué aprendí

- **LCEL es el idioma de LangChain.** Pensar en `|` (componer pasos) hace que el código se lea como el diagrama del flujo.
- Separar **system / human** en el prompt es la base para inyectar contexto sin ensuciar las instrucciones.
- `gpt-4o-mini` es ideal para *playground*: suficientemente bueno y suficientemente barato para iterar sin miedo a la factura.

🔗 **Ver el código en GitHub:** [learning/courses/RAG-LangChain-LlamaIndex](https://github.com/igorparrabastias/igorparrabastias.github.io/tree/main/learning/courses/RAG-LangChain-LlamaIndex)
