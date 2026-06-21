## Más allá del texto: modelos multimodales

Durante años, los grandes modelos de lenguaje vivieron en un mundo hecho solo de palabras. Pero el mundo real no es así: combinamos texto, imágenes, sonidos, gestos y diagramas para comunicarnos. La **multimodalidad** es, precisamente, la capacidad de un modelo para procesar y/o generar información en varias **modalidades** (formas de datos) distintas: no solo texto, sino también imágenes, audio, vídeo o código. Importa porque acerca la inteligencia artificial al modo en que los humanos percibimos: un asistente que "ve" una foto de un error en pantalla, "escucha" una pregunta hablada y responde por escrito resulta mucho más útil que uno limitado a un único canal.

### Cómo entra el mundo en el modelo

La gran idea que hace posible la multimodalidad es la conversión de cualquier dato a **tokens** o vectores numéricos que el Transformer pueda procesar de manera uniforme. El reto es traducir cada modalidad a esa "lengua común" de números.

#### Visión

Para la **visión**, la técnica dominante es el **Vision Transformer** (ViT, *Transformador de Visión*). En lugar de leer la imagen píxel a píxel, se divide en una cuadrícula de **parches** (*patches*), por ejemplo cuadrados de 16x16 píxeles. Cada parche se aplana y se proyecta a un vector, de forma análoga a como una palabra se convierte en un *embedding*. La secuencia de parches entra entonces en un Transformer estándar, que usa la **atención** para relacionar unas regiones de la imagen con otras. Así, una imagen se trata como "una frase de parches".

#### Audio y código

El **audio** suele transformarse primero en un **espectrograma** (una representación visual de las frecuencias a lo largo del tiempo) que puede tratarse casi como una imagen, o bien se trocea la onda en fragmentos cortos que se convierten en tokens acústicos. El **código** fuente, por su parte, es texto, pero con estructura muy marcada (sintaxis, sangrías, símbolos): los modelos lo aprenden mejor cuando se entrenan específicamente con grandes repositorios de programas, capturando patrones de funciones, variables y errores comunes.

### Un espacio común: embeddings compartidos

El verdadero salto conceptual es lograr que distintas modalidades compartan un mismo **espacio de representación**. El ejemplo canónico es **CLIP** (*Contrastive Language-Image Pre-training*, preentrenamiento contrastivo de lenguaje e imagen), de OpenAI. CLIP entrena en paralelo dos codificadores, uno para texto y otro para imágenes, usando millones de pares (imagen, descripción) recogidos de la web. El objetivo del entrenamiento **contrastivo** es sencillo de enunciar: acercar en el espacio vectorial los pares que sí van juntos (una foto de un perro y el texto "un perro") y alejar los que no.

El resultado es un **espacio de embeddings compartido**: la imagen de un gato y la palabra "gato" caen en posiciones cercanas, aunque provengan de modalidades distintas. Esto permite, por ejemplo, buscar imágenes con una frase, o clasificar fotos sin haber sido entrenado explícitamente para cada categoría (capacidad llamada *zero-shot*, "sin ejemplos previos").

### Modelos nativos multimodales y "any-to-any"

Los primeros sistemas multimodales eran, en realidad, varios modelos pegados: un codificador de imagen conectado a un modelo de lenguaje. Los modelos **nativos multimodales** dan un paso más: se entrenan desde el principio con múltiples modalidades mezcladas, de modo que la comprensión conjunta no es un añadido sino parte de su naturaleza. Ejemplos como **GPT-4o** (la "o" de *omni*) o **Gemini** se diseñaron para aceptar texto, imágenes y audio de forma integrada.

La frontera siguiente es lo que se denomina **"any-to-any"** (de cualquier modalidad a cualquier modalidad): un único modelo que recibe entradas en varias modalidades y también **genera** salidas en varias de ellas. Un sistema así puede escuchar una pregunta hablada, mirar una imagen adjunta y responder con voz o con una imagen nueva, todo dentro del mismo flujo. Esto reduce la latencia y conserva matices (como el tono de voz) que se perderían al traducir todo a texto intermedio.

### Generar imágenes y vídeo: la difusión

Generar texto y generar imágenes funcionan de manera distinta. Los modelos de texto son **autoregresivos**: producen un token tras otro, prediciendo la siguiente palabra según las anteriores. La imagen y el vídeo, en cambio, suelen crearse con **modelos de difusión** (*diffusion models*).

La intuición de la **difusión** es la siguiente: durante el entrenamiento se toma una imagen real y se le añade ruido progresivamente hasta convertirla en puro "estática". El modelo aprende a invertir ese proceso, es decir, a **quitar ruido** paso a paso. Para generar, se parte de ruido aleatorio y el modelo lo va refinando, guiado por un texto descriptivo (el *prompt*), hasta hacer emerger una imagen coherente. El vídeo extiende la idea añadiendo coherencia temporal entre fotogramas. La diferencia clave frente a los modelos de texto es, pues, **generación iterativa por refinamiento global** (difusión) frente a **generación secuencial token a token** (autoregresiva).

## Evaluación, seguridad y alineación

Construir modelos potentes es solo la mitad del problema; la otra mitad es saber **cómo de buenos y de seguros** son realmente. Esta sección aborda cómo se miden, cómo fallan y cómo se intenta alinearlos con los valores humanos.

### Benchmarks: medir es más difícil de lo que parece

Un **benchmark** (banco de pruebas) es un conjunto estandarizado de tareas con respuestas conocidas que permite comparar modelos. Algunos muy citados son:

- **MMLU** (*Massive Multitask Language Understanding*): miles de preguntas tipo test sobre 57 materias, desde historia hasta medicina, para medir conocimiento general.
- **GPQA** (*Graduate-level Google-Proof Q&A*): preguntas de nivel de posgrado en ciencias, diseñadas para que ni siquiera buscando en internet sean fáciles.
- **HumanEval**: problemas de programación en los que el modelo debe escribir código que pase pruebas automáticas, midiendo capacidad de generar **código** funcional.

Evaluar bien es sorprendentemente difícil por dos problemas centrales. La **saturación** ocurre cuando los mejores modelos rozan el 100 % de aciertos: el benchmark deja de distinguir entre ellos y pierde utilidad. La **contaminación de datos** (*data contamination*) sucede cuando las preguntas del test aparecieron, sin querer, en los datos de entrenamiento; entonces el modelo "recuerda" la respuesta en lugar de razonarla, inflando su puntuación. Por eso la comunidad crea continuamente benchmarks nuevos, privados o resistentes a la memorización, y desconfía de comparaciones basadas en una sola cifra.

### Cómo fallan los modelos

Incluso los mejores sistemas presentan fallos característicos:

- **Alucinaciones**: el modelo genera información falsa con total seguridad y fluidez, por ejemplo citas o datos inexistentes. Surge porque está entrenado para producir texto plausible, no necesariamente verdadero.
- **Sesgos**: al aprender de datos humanos, el modelo puede reproducir o amplificar prejuicios sociales presentes en ellos.
- **Jailbreaks**: técnicas que, mediante instrucciones astutas (juegos de rol, hipótesis, idiomas raros), logran que el modelo eluda sus normas de seguridad y produzca contenido prohibido.
- **Inyección de prompts** (*prompt injection*): un atacante esconde instrucciones maliciosas dentro de datos que el modelo va a leer (una página web, un correo, un documento), logrando que el sistema obedezca al atacante en vez de al usuario legítimo. Es especialmente peligroso en agentes con acceso a herramientas.

### Alineación: que el modelo quiera lo correcto

La **alineación** (*alignment*) busca que el comportamiento del modelo concuerde con las intenciones y valores humanos. Las técnicas ya vistas, **RLHF** (aprendizaje por refuerzo con retroalimentación humana) y la **IA Constitucional** (*Constitutional AI*), son piezas clave de este esfuerzo. A ellas se suman otras prácticas:

- **Red-teaming**: equipos de personas (o de otros modelos) atacan deliberadamente el sistema para encontrar fallos, jailbreaks y conductas peligrosas antes de que lo hagan usuarios malintencionados.
- **Interpretabilidad mecanicista** (*mechanistic interpretability*): línea de investigación que intenta abrir la "caja negra" y entender los **circuitos internos** del modelo, es decir, qué neuronas y qué patrones de activación implementan cada comportamiento. La meta es pasar de observar qué hace el modelo a comprender por qué lo hace, lo que permitiría detectar engaños o intenciones ocultas a nivel de mecanismo.

### Gobernanza y regulación

Más allá de lo técnico, existe un creciente esfuerzo de **gobernanza**. La iniciativa más destacada es el **EU AI Act** (Reglamento de Inteligencia Artificial de la Unión Europea), aprobado en 2024, que clasifica los sistemas según su **nivel de riesgo** e impone obligaciones más estrictas a los usos de alto riesgo y a los modelos de propósito general más capaces. En paralelo, gobiernos y laboratorios debaten sobre transparencia, evaluaciones obligatorias de seguridad y posibles límites a los modelos de frontera. El **debate sobre seguridad** enfrenta dos preocupaciones legítimas: por un lado, riesgos presentes (desinformación, sesgos, abusos); por otro, riesgos futuros de sistemas mucho más capaces. No hay consenso, pero sí un acuerdo amplio en que la potencia creciente de estos modelos exige medir, vigilar y regular con seriedad.
