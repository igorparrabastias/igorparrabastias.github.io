# RAG Skyline Agent 🟢

> Proyecto **propio**. Un chatbot RAG con arquitectura **hexagonal (puertos y adaptadores)**, escrito como ejercicio para llevar la teoría del PLN al código real. Encaja como el "siguiente paso" de la serie [Fundamentos del PLN y la IA](../fundamento-del-pln-y-la-ia.md): después de entender *qué* es un LLM y *cómo* recupera contexto, aquí se ve *cómo se construye* uno mantenible.

## De la teoría al código

En la serie de historia del PLN explico el arco que va de las representaciones simbólicas a los LLM y el patrón **RAG** (Retrieval-Augmented Generation): el modelo no "sabe" tus datos privados, así que los **recuperamos** de una fuente externa y se los inyectamos en el prompt. Este proyecto materializa ese patrón con un caso concreto: el **agente de atención al cliente de una aerolínea ficticia, SkyFlow Airlines**.

El ejercicio (ver el `README.md` del proyecto) plantea tres comportamientos:

1. El bot empieza con *small talk* y consultas no confidenciales.
2. Cuando el usuario pregunta por datos protegidos (su vuelo), el bot **pide la información necesaria** para identificarlo.
3. Cuando la recuperación tiene éxito, el agente puede hablar de la información de la base de datos.

> [!TIP]
> Es básicamente un recepcionista con muy buena memoria a corto plazo y cero acceso a tus datos hasta que le das tu número de confirmación. Como en la vida real, pero sin la música de espera. 🎧

## La arquitectura hexagonal en 30 segundos

La idea de **puertos y adaptadores** es separar el **dominio** (la lógica que no debería cambiar si mañana cambias de LLM o de interfaz) de los **detalles** (Gradio, OpenAI, la base de datos). El dominio define *qué* necesita; los adaptadores aportan el *cómo*.

```
src/
├── core/                 # Dominio: la lógica RAG, agnóstica de tecnología
│   ├── pipeline.py       #   orquesta las dos cadenas (interna y externa)
│   ├── knowledge_base.py #   esquema Pydantic del estado de la conversación
│   ├── prompt.py         #   plantillas de prompt (system / parser)
│   └── extractor.py      #   "slot filling" estructurado con Pydantic
├── adapters/             # Adaptadores: el mundo exterior
│   ├── gradio_adapter.py #   UI web de chat
│   ├── console_adapter.py#   pretty-print para depurar en terminal
│   └── llm_adapter.py    #   el LLM concreto (ChatOpenAI / gpt-4o-mini)
├── infrastructure/
│   └── database.py       #   recuperación de datos de vuelo (simulada)
├── preprocessors/
│   └── text_cleaner.py   #   limpieza de texto
├── config.py             # carga de variables de entorno (.env)
└── main.py               # punto de entrada: cablea todo y lanza Gradio
```

El truco mental: si quisieras cambiar Gradio por una API REST, o `gpt-4o-mini` por otro modelo, solo tocas un adaptador. El `core/` ni se entera.

## El corazón: dos cadenas de LangChain

Todo el flujo vive en `pipeline.py`. Hay **dos cadenas** que conviene distinguir:

- La **cadena interna** (`internal_chain`) actualiza el *estado* de la conversación: extrae lo que el usuario ha dicho (nombre, apellido, número de confirmación) y consulta la base de datos.
- La **cadena externa** (`external_chain`) genera la respuesta visible para el usuario, con ese estado ya enriquecido inyectado en el prompt.

```python
--8<-- "learning/AI/rag-skyline-agent/src/core/pipeline.py"
```

`RunnableAssign` es la pieza clave: va **añadiendo claves al diccionario de estado** que fluye por la cadena. Primero `know_base` (lo que sabemos del usuario), luego `context` (lo recuperado de la base de datos). Eso es RAG en miniatura: *recuperar → aumentar el prompt → generar*.

## El estado: una base de conocimiento tipada

¿Qué recordamos de la conversación? Lo define un modelo **Pydantic**, lo que nos da validación y, sobre todo, un **esquema** que el LLM puede rellenar:

```python
--8<-- "learning/AI/rag-skyline-agent/src/core/knowledge_base.py"
```

El `extractor.py` usa este esquema con un `PydanticOutputParser`: en cada turno, el LLM **relee la conversación y rellena los huecos** (*slot filling*). Si el usuario dice "soy Jane Doe, confirmación 12345", esos campos aparecen poblados en el siguiente paso, y entonces `database_getter` (en `infrastructure/database.py`) puede buscar el vuelo. Mientras falten datos, el bot los pide; cuando están, recupera y responde. Así se implementan los tres comportamientos del ejercicio sin un solo `if` gigante: el estado tipado guía la conversación.

## El adaptador de interfaz: Gradio

El dominio no sabe que existe una web. El adaptador de Gradio toma la función generadora `chat_gen` y la envuelve en un `ChatInterface` con *streaming*:

```python
--8<-- "learning/AI/rag-skyline-agent/src/adapters/gradio_adapter.py"
```

Hay dos variantes a propósito: `launch_gradio_chatbot` (la UI real) y `queue_fake_streaming_gradio` (un bucle de terminal que *imita* a Gradio para depurar sin levantar el navegador). Mismo dominio, dos adaptadores.

## Cómo se cablea todo: `main.py`

El punto de entrada es donde la arquitectura "se nota": crea el estado, define `chat_gen` (que invoca la cadena interna y luego *streamea* la externa) y lanza el adaptador elegido.

```python
--8<-- "learning/AI/rag-skyline-agent/src/main.py"
```

Fíjate en el patrón: `internal_chain.invoke(state)` actualiza el estado, se imprime para diagnóstico, y `external_chain.stream(state)` produce la respuesta token a token.

## El resto de piezas

- **`core/prompt.py`** — dos plantillas: `external_prompt` (la personalidad del agente de SkyFlow, con `{know_base}` y `{context}` inyectados) y `parser_prompt` (instruye al LLM para rellenar el esquema Pydantic).
- **`core/extractor.py`** — la función `RExtract`, que monta la cadena de extracción estructurada y hace un *preparse* defensivo del JSON que devuelve el modelo (un clásico: los LLM a veces se comen una llave `{`).
- **`infrastructure/database.py`** — una "base de datos" simulada de vuelos en memoria; el punto de extensión natural para conectar una BD real.
- **`adapters/llm_adapter.py`** — una sola línea que aísla `ChatOpenAI(model="gpt-4o-mini")`. Cambiar de proveedor es cambiar este archivo.
- **`adapters/console_adapter.py`** y **`preprocessors/text_cleaner.py`** — utilidades de *pretty-print* y limpieza de texto.

## Qué aprendí

- **RAG no es magia**: es estado + recuperación + un prompt bien construido. Verlo como "ir añadiendo claves a un diccionario" lo desmitifica.
- La **arquitectura hexagonal** brilla justo en proyectos de IA, donde los detalles (modelo, UI, vector store) cambian cada semana pero la lógica de conversación no.
- El **slot filling con Pydantic** es una forma elegante y robusta de mantener memoria estructurada sin reinventar el parsing.

🔗 **Ver el código en GitHub:** [learning/AI/rag-skyline-agent](https://github.com/igorparrabastias/igorparrabastias.github.io/tree/main/learning/AI/rag-skyline-agent)
