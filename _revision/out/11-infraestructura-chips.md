## La infraestructura: chips, cómputo y energía detrás de los LLM

Detrás de cada respuesta de un **LLM** (*Large Language Model*, modelo de lenguaje de gran tamaño) hay una maquinaria física descomunal. Entender esa infraestructura ayuda a explicar por qué estos sistemas son caros de entrenar, por qué solo unas pocas organizaciones los construyen desde cero y por qué su despliegue tiene implicaciones energéticas y ambientales relevantes. En esta sección dejamos de lado las matemáticas del modelo para mirar el **hardware** y los **sistemas** que lo hacen posible.

### Por qué GPUs y no CPUs

El entrenamiento y la inferencia de un LLM consisten, en lo esencial, en **multiplicar matrices** una y otra vez: miles de millones de operaciones de álgebra lineal por cada paso. Estas operaciones son altamente **paralelizables**, es decir, muchas se pueden ejecutar a la vez sin depender unas de otras.

Una **CPU** (*Central Processing Unit*, unidad central de procesamiento) tiene pocos núcleos muy potentes, optimizados para tareas secuenciales y diversas. Una **GPU** (*Graphics Processing Unit*, unidad de procesamiento gráfico) tiene miles de núcleos más sencillos diseñados para hacer la misma operación sobre grandes bloques de datos simultáneamente. Para el álgebra matricial de las redes neuronales, esa arquitectura masivamente paralela encaja a la perfección, y por eso la GPU se convirtió en el caballo de batalla de la inteligencia artificial.

El fabricante dominante es **NVIDIA**, cuyas GPUs de centro de datos marcaron la última década: la **A100** (arquitectura Ampere), la **H100** y la **H200** (arquitectura Hopper) y, más recientemente, la generación **Blackwell** con chips como el **B200**. Cada generación incrementa la potencia de cómputo, pero también mejora algo que a menudo importa más: la **memoria**.

#### El "muro de memoria" y la HBM

Para procesar un modelo, la GPU debe tener sus parámetros y datos intermedios accesibles en una memoria muy rápida. Aquí entra la **HBM** (*High Bandwidth Memory*, memoria de alto ancho de banda), un tipo de memoria apilada físicamente junto al chip que ofrece un **ancho de banda** enorme, es decir, mueve datos hacia y desde los núcleos a una velocidad altísima.

El problema es que, con frecuencia, los núcleos de cómputo terminan de calcular antes de que la memoria les entregue los siguientes datos: quedan **esperando**. A este desequilibrio entre la velocidad de cálculo y la de movimiento de datos se le llama **muro de memoria** (*memory wall*). En la práctica, muchas cargas de trabajo de LLM no están limitadas por cuántas operaciones puede hacer la GPU, sino por cuán rápido puede alimentarla la memoria. Por eso la cantidad y el ancho de banda de HBM son a menudo el factor decisivo al elegir hardware, más que la potencia bruta de cálculo.

### Alternativas: un ecosistema que se diversifica

Aunque NVIDIA domina, el mercado se ha ido diversificando:

- **TPU** (*Tensor Processing Unit*, unidad de procesamiento de tensores): chips diseñados por **Google** específicamente para redes neuronales. Google los usa internamente y los ofrece en su nube.
- **AMD** compite con su línea **Instinct**, en particular el acelerador **MI300**, que apuesta fuerte por la capacidad de memoria.
- **Aceleradores especializados en inferencia**: empresas como **Groq** (con sus *LPU*, unidades de procesamiento de lenguaje) o **Cerebras** (con chips de escala de oblea, *wafer-scale*) buscan ofrecer respuestas más rápidas o más baratas que una GPU convencional, optimizando para la fase de uso del modelo más que para su entrenamiento.

Esta variedad refleja una tendencia: a medida que la demanda crece, aparecen diseños adaptados a nichos concretos en lugar de un único chip que sirva para todo.

### Interconexión: cuando comunicar es el cuello de botella

Un LLM moderno no se entrena en una sola GPU, sino en **clusters** de miles a decenas de miles de ellas trabajando coordinadas. Y aquí surge un problema central de los sistemas distribuidos: las GPUs deben **intercambiar datos constantemente** entre sí, y ese intercambio puede convertirse en el verdadero cuello de botella.

Para mitigarlo se usan interconexiones de muy alta velocidad:

- **NVLink**: conexión directa y rápida entre GPUs dentro de un mismo servidor o conjunto cercano de servidores.
- **InfiniBand**: red de baja latencia y alto ancho de banda que conecta servidores entre sí dentro del centro de datos.

La intuición clave es esta: si cientos de chips deben sincronizar resultados parciales en cada paso del entrenamiento, una red lenta hace que todos esperen al más rezagado. Por eso la **comunicación** entre chips se diseña con tanto cuidado como el cómputo en sí; un cluster mal interconectado desperdicia gran parte de su potencia teórica.

### Paralelismo de entrenamiento: por qué el modelo no cabe en una GPU

Los modelos grandes tienen tantos parámetros que sus pesos, sus gradientes y los datos intermedios **no caben en la memoria de una sola GPU**. La solución es repartir el trabajo, y existen tres estrategias conceptuales que suelen combinarse:

- **Paralelismo de datos** (*data parallelism*): cada GPU tiene una **copia completa** del modelo y procesa una porción distinta de los datos. Luego las GPUs combinan sus resultados para actualizar los pesos de forma coherente. Sirve para acelerar, pero requiere que el modelo entero quepa en cada GPU.
- **Paralelismo de tensores** (*tensor parallelism*): una **misma operación matricial** se reparte entre varias GPUs, cada una calculando un trozo. Permite alojar capas que individualmente no caben en un solo chip, a costa de mucha comunicación.
- **Paralelismo de pipeline** (*pipeline parallelism*): las **capas** del modelo se distribuyen entre grupos de GPUs, como una cadena de montaje; los datos avanzan por etapas y cada grupo se encarga de un tramo de la red.

En los entrenamientos reales se mezclan los tres (lo que a veces se denomina *paralelismo 3D*) para equilibrar memoria, cómputo y comunicación. Coordinar todo esto es un reto de ingeniería de sistemas tan exigente como el propio aprendizaje automático.

### Costos: entrenamiento e inferencia

El **entrenamiento** de un LLM de frontera implica miles de GPUs funcionando de forma continua durante semanas o meses. Sumando el hardware, la electricidad y el personal, el coste de una sola corrida de entrenamiento de un modelo grande está, según estimaciones públicas, **del orden de decenas a cientos de millones de USD** para los modelos más ambiciosos. Conviene tomar estas cifras como **órdenes de magnitud**, no como números exactos, porque dependen de muchísimos factores y rara vez se publican con detalle.

Un punto que suele pasarse por alto: la **inferencia** —usar el modelo ya entrenado para responder— también es cara, pero de otra manera. El entrenamiento es un gasto **único** (o periódico); la inferencia se paga **en cada consulta**, multiplicada por millones de usuarios. A escala global, el coste acumulado de servir un modelo popular puede superar al de haberlo entrenado. Por eso optimizar la inferencia tiene un enorme valor económico.

### Energía y medio ambiente

Toda esta capacidad de cómputo consume **electricidad** en cantidades enormes, y los chips generan calor que hay que disipar, lo que a su vez requiere sistemas de refrigeración que consumen **agua** y más energía. Los grandes centros de datos dedicados a IA tienen demandas eléctricas comparables a las de pequeñas ciudades, y la tendencia es claramente **creciente**: cada nueva generación de modelos y el aumento del número de usuarios empujan la demanda hacia arriba.

Esto plantea desafíos de **sostenibilidad** reales: presión sobre las redes eléctricas, huella de carbono según el origen de la energía, y consumo de agua en regiones donde puede ser un recurso escaso. Las respuestas en marcha incluyen el uso de energías renovables, hardware más eficiente por operación y técnicas de refrigeración avanzadas, pero el balance ambiental sigue siendo un tema abierto y de creciente atención pública y regulatoria.

### Optimización de inferencia

Dado el peso económico y energético de servir modelos, se han desarrollado numerosas técnicas para hacer la inferencia más eficiente:

- **Batching** (agrupamiento): juntar varias consultas y procesarlas a la vez aprovecha mejor el paralelismo de la GPU, repartiendo el coste fijo entre muchas peticiones.
- **KV-cache** (caché de claves y valores): durante la generación de texto, el modelo reutiliza cálculos intermedios de los tokens ya generados en lugar de recomputarlos, lo que acelera notablemente la producción de cada nueva palabra.
- **Cuantización**: representar los pesos con menos bits reduce la memoria necesaria y el tráfico de datos, aliviando el muro de memoria (tratada en detalle en otra sección).
- **Decodificación especulativa** (*speculative decoding*): un modelo pequeño y rápido propone varios tokens que un modelo grande **verifica** de golpe, acelerando la generación cuando las propuestas aciertan.
- **Destilación** (*distillation*): entrenar un modelo más pequeño para que imite a uno grande, obteniendo un sistema más barato de servir con una pérdida de calidad acotada (también se aborda por separado).

En conjunto, estas técnicas explican por qué un mismo modelo puede ofrecerse hoy con latencias y costes muy distintos: gran parte de la innovación reciente en LLM no ocurre solo en el modelo, sino en la **infraestructura y los sistemas** que lo rodean.
