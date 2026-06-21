## Agentes: LLM que razonan, usan herramientas y actúan

En capítulos anteriores presentamos la idea de **agente** como un sistema que utiliza un **LLM** (*Large Language Model*, modelo de lenguaje grande) como motor de razonamiento para planificar y usar herramientas. Aquí profundizamos en cómo funciona realmente esa maquinaria: el ciclo que conecta el lenguaje con la acción, los patrones de planificación, la memoria, los protocolos emergentes y los riesgos que aparecen cuando un modelo deja de limitarse a hablar y empieza a actuar.

### De chatbot a agente

Conviene distinguir dos modos de uso del mismo modelo. Un **chatbot** recibe un mensaje y devuelve una respuesta en texto: su único efecto sobre el mundo es producir palabras. Es reactivo y autónomo en un solo paso; si le pides reservar un vuelo, te explicará cómo hacerlo, pero no lo hará.

Un **agente**, en cambio, persigue un **objetivo** a lo largo de **varios pasos**. No solo genera texto: decide *qué hacer a continuación*, ejecuta acciones a través de herramientas, observa los resultados y ajusta su plan. La diferencia clave es la presencia de un **bucle de control** y de la capacidad de **actuar** sobre un entorno (un sistema de ficheros, una API, un navegador, una base de datos). El chatbot responde; el agente ejecuta tareas.

### Uso de herramientas y *function calling*

El mecanismo central que convierte a un LLM en agente es el **uso de herramientas**, conocido técnicamente como **function calling** (invocación de funciones). La idea es sencilla pero poderosa: además del texto del usuario, se le entrega al modelo una lista de **herramientas disponibles**, cada una descrita mediante un **esquema** en formato **JSON** (*JavaScript Object Notation*) con su nombre, una descripción en lenguaje natural y los parámetros que acepta.

Cuando el modelo determina que necesita información o una acción externa para avanzar, en lugar de responder con texto produce una **llamada estructurada**: indica qué herramienta usar y con qué argumentos. Un esquema de herramienta puede tener este aspecto:

```json
{
  "name": "buscar_clima",
  "description": "Devuelve el tiempo actual de una ciudad",
  "parameters": {
    "type": "object",
    "properties": {
      "ciudad": { "type": "string" },
      "unidades": { "type": "string", "enum": ["celsius", "fahrenheit"] }
    },
    "required": ["ciudad"]
  }
}
```

Es importante entender que **el modelo no ejecuta la función**: solo *propone* la llamada. El código que envuelve al modelo (el llamado **arnés** o *runtime* del agente) recibe esa propuesta, ejecuta la función de verdad y le devuelve el resultado al modelo como una nueva entrada, la **observación**. Así se cierra el **bucle**:

```text
  Objetivo del usuario
        |
        v
  +-----------------+
  |  PERCEPCIÓN     |  <-- contexto + observaciones previas
  +-----------------+
        |
        v
  +-----------------+
  |  RAZONAMIENTO   |  ¿Tengo la respuesta o necesito una herramienta?
  +-----------------+
        |
   ¿accion?  --- no ---> RESPUESTA FINAL
        | sí
        v
  +-----------------+
  |  ACCIÓN         |  llamada a herramienta (JSON)
  +-----------------+
        |
        v
  +-----------------+
  |  OBSERVACIÓN    |  resultado de la herramienta
  +-----------------+
        |
        +----> vuelve a PERCEPCIÓN (repite)
```

Este ciclo **percepción → razonamiento → acción → observación** se repite hasta que el modelo decide que la tarea está completa y emite una respuesta final.

### El patrón ReAct: razonar y actuar

El patrón **ReAct** (de *Reasoning + Acting*, razonar y actuar) formaliza esta dinámica intercalando, paso a paso, **pensamientos** explícitos y **acciones**. En cada iteración el modelo escribe un breve razonamiento ("para responder esto necesito buscar X"), emite una acción (la llamada a herramienta) y luego incorpora la observación antes de pensar de nuevo. Hacer visible el razonamiento mejora la fiabilidad y, además, facilita la depuración, porque el desarrollador puede leer la cadena de decisiones.

Sobre esta base se construyen capacidades más avanzadas:

- **Planificación y descomposición de tareas**: ante un objetivo complejo, el agente lo divide en **subtareas** más manejables y las aborda en orden. Algunos sistemas generan primero un plan completo y luego lo ejecutan; otros planifican de forma incremental, paso a paso.
- **Auto-corrección**: cuando una acción falla o una observación contradice lo esperado (un error de una API, un test que no pasa), el agente puede **reflexionar** sobre el fallo y reintentar con una estrategia distinta, en lugar de continuar ciegamente.

### Memoria: contexto inmediato y largo plazo

Un agente necesita **recordar**. Conviene distinguir dos niveles.

La **memoria inmediata** o de trabajo es la **ventana de contexto** del modelo: todo lo que cabe en la entrada actual (instrucciones, historial reciente, observaciones). Es rápida y precisa, pero **limitada** en tamaño; cuando una tarea se alarga, no todo cabe.

La **memoria a largo plazo** resuelve esa limitación almacenando información fuera del modelo para recuperarla cuando haga falta. La técnica habitual usa **almacenes vectoriales** (*vector stores*): los textos se convierten en **embeddings** (vectores numéricos que capturan su significado) y se guardan en una base de datos especializada. Cuando el agente necesita recordar algo relevante, busca por **similitud semántica** y trae solo los fragmentos pertinentes al contexto. Es la misma maquinaria que sustenta el **RAG** (*Retrieval-Augmented Generation*, generación aumentada por recuperación) visto antes, ahora puesta al servicio de la memoria del agente.

### Protocolos y estandarización

A medida que proliferaban las integraciones, conectar cada modelo con cada herramienta o fuente de datos se volvió un trabajo repetitivo y frágil. De ahí el interés por **estandarizar** la conexión. Un ejemplo destacado, presentado a finales de 2024 por Anthropic y adoptado ampliamente durante 2025, es el **MCP** (*Model Context Protocol*, protocolo de contexto del modelo): un estándar abierto que define cómo un asistente descubre y usa herramientas y datos externos a través de **servidores** que exponen esas capacidades de forma uniforme. La analogía habitual es la de un "puerto universal": en vez de un conector a medida por cada integración, un mismo protocolo permite enchufar de manera homogénea sistemas de archivos, repositorios, bases de datos o aplicaciones de terceros. La estandarización reduce el esfuerzo de integración y favorece un ecosistema de herramientas reutilizables.

### Sistemas multi-agente

En lugar de un único agente que lo hace todo, a veces es más eficaz repartir el trabajo entre varios **agentes especializados** con **roles** distintos que **colaboran**. Por ejemplo, un agente "investigador" recopila información, un agente "redactor" la sintetiza y un agente "revisor" la verifica. A menudo un **orquestador** coordina al conjunto: descompone el objetivo, reparte subtareas y combina los resultados.

Las ventajas son la **modularidad** y la **especialización**: cada agente puede tener sus propias herramientas e instrucciones. Las desventajas son el **coste** (más llamadas al modelo), la mayor **latencia** y la dificultad de coordinación, ya que los errores de un agente pueden propagarse a los demás.

### *Computer use*: agentes que operan interfaces

Una frontera reciente es el **computer use** (uso del ordenador): agentes capaces de operar **interfaces gráficas** y **navegadores** como lo haría una persona. En vez de llamar a una API, el agente recibe una **captura de pantalla**, razona sobre lo que ve y emite acciones de bajo nivel: mover el cursor, hacer clic, escribir texto, desplazarse. Esto le permite manejar aplicaciones que no ofrecen una interfaz programable. La contrapartida es que es **más lento y más frágil** que una API, y sus errores pueden tener efectos visibles directos sobre el sistema.

### Aplicaciones y límites

Los agentes ya muestran utilidad práctica en varios frentes: **asistentes de programación** que leen un repositorio, escriben código, ejecutan pruebas y corrigen errores; **investigación** automatizada que busca, lee y sintetiza fuentes; y **automatización** de flujos de trabajo administrativos repetitivos.

No obstante, sus **límites y riesgos** son serios y conviene tenerlos presentes:

- **Fiabilidad y errores que se componen**: cada paso tiene una probabilidad de fallo, y en una cadena larga esos pequeños errores **se acumulan**, de modo que la fiabilidad total cae rápidamente con el número de pasos.
- **Bucles**: un agente puede quedar atrapado repitiendo la misma acción fallida sin progresar; por eso suelen imponerse **límites** de iteraciones o de coste.
- **Seguridad**. La **inyección de prompts** (*prompt injection*) es especialmente peligrosa: contenido malicioso oculto en una página web o un documento puede secuestrar las instrucciones del agente y hacerle ejecutar acciones no deseadas. Y como el agente **actúa**, puede provocar **acciones irreversibles** (borrar datos, enviar dinero, publicar información).

Por todo ello, el diseño responsable de agentes incorpora salvaguardas: **permisos acotados**, **confirmación humana** para operaciones sensibles, **límites** de ejecución y **registros** auditables. La autonomía es valiosa, pero debe concederse de forma gradual y supervisada.
