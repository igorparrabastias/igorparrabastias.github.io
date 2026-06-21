## Cómo funcionan los LLM hoy: del texto al token y de vuelta

Un **gran modelo de lenguaje** (*Large Language Model*, LLM) no manipula texto directamente: lo convierte en una secuencia de números, opera sobre ellos y, al final, vuelve a traducirlos en texto. Conviene recorrer ese viaje completo —del texto al token y de vuelta— porque ahí se esconden casi todas las decisiones de diseño que explican el comportamiento, el coste y las limitaciones de estos sistemas. Damos por conocidas la arquitectura **Transformer** y la atención, que se trataron antes; aquí nos centramos en el resto del proceso moderno.

### Tokenización: la unidad mínima

Antes de que el modelo vea nada, el texto se divide en **tokens**: trozos que no son ni palabras completas ni caracteres sueltos, sino **subpalabras**. La técnica dominante es **BPE** (*Byte Pair Encoding*, codificación por pares de bytes), a menudo en su variante **byte-level**, que trabaja sobre los bytes crudos del texto y por eso puede representar cualquier carácter Unicode, emoji o símbolo sin "quedarse fuera de vocabulario".

¿Por qué no usar palabras? Porque el vocabulario sería gigantesco e incapaz de manejar palabras nuevas, erratas o lenguas con morfología rica. ¿Y por qué no caracteres? Porque las secuencias serían larguísimas y el modelo gastaría capacidad en aprender a formar palabras desde cero. Las subpalabras son el punto intermedio: las cadenas frecuentes ("agua", "ción") se vuelven un único token, mientras que las raras se descomponen en piezas más pequeñas. Un vocabulario típico es del orden de **100.000 tokens**.

Esto tiene consecuencias muy prácticas:

- **Idiomas no ingleses.** Los vocabularios suelen optimizarse con datos mayoritariamente en inglés, así que el mismo contenido en español, y más aún en lenguas con otros alfabetos, consume **más tokens**. Eso encarece el procesamiento y reduce el texto efectivo que cabe en el contexto.
- **Números.** Una cifra como `2025` puede partirse en varios tokens de forma poco intuitiva, lo que explica parte de las dificultades históricas de los LLM con la aritmética.
- **Coste.** Tanto el precio de las API como los límites de longitud se miden **en tokens**, no en palabras ni caracteres. Como regla aproximada, en inglés un token equivale a unos tres cuartos de palabra; en español, algo menos.

### Preentrenamiento: predecir el siguiente token a escala

El corazón del aprendizaje es sorprendentemente simple. Durante el **preentrenamiento**, el modelo recibe enormes cantidades de texto y se entrena en una sola tarea: **predecir el siguiente token** dado todo lo anterior. No hay etiquetas humanas; la "respuesta correcta" es, sencillamente, el token que de verdad venía a continuación. Por eso se habla de aprendizaje **autosupervisado**.

Matemáticamente, se minimiza la **entropía cruzada** entre la distribución que predice el modelo y el token real:

```
L = - (1/N) · Σ_i  log P(t_i | t_1, ..., t_{i-1}; θ)
```

Donde cada símbolo significa:

- `L` es la **pérdida** (*loss*) que se quiere reducir; cuanto menor, mejor predice el modelo.
- `N` es el número de tokens considerados.
- `t_i` es el token en la posición `i`, y `t_1, ..., t_{i-1}` es todo el contexto previo.
- `P(t_i | ...)` es la probabilidad que el modelo asigna al token correcto.
- `θ` (theta) son los **parámetros** del modelo (sus pesos).
- `Σ_i` indica que se suma sobre todas las posiciones, y el logaritmo penaliza con dureza asignar baja probabilidad al token verdadero.

Los datos provienen de fuentes muy variadas: páginas **web** filtradas, **código** fuente, **libros**, artículos y enciclopedias. Las magnitudes son enormes: los modelos punteros se entrenan con del orden de **billones de tokens** (en la escala europea, millones de millones), tienen desde **miles de millones** hasta cientos de miles de millones de **parámetros**, y consumen cantidades de **cómputo** que se miden en miles de unidades de procesamiento gráfico funcionando durante semanas o meses.

La pregunta natural es: ¿cómo puede "predecir la siguiente palabra" producir un sistema que razona, traduce y programa? La intuición es que, para acertar el siguiente token de forma sistemática sobre textos tan diversos, el modelo se ve **obligado** a aprender estructuras subyacentes: gramática, hechos del mundo, estilos, relaciones lógicas y hasta esbozos de razonamiento. Predecir bien el final de "El teorema de Pitágoras dice que..." exige, de hecho, haber capturado el teorema. La tarea es trivial de enunciar, pero resolverla a gran escala empuja al modelo a comprimir una porción asombrosa del conocimiento humano en sus pesos.

### Post-entrenamiento: de loro estadístico a asistente útil

Un **modelo base**, recién salido del preentrenamiento, no es directamente útil. Sabe **continuar** texto, pero no **seguir instrucciones**: si le pides "Explícame la fotosíntesis", podría responder con otra pregunta similar, porque eso es lo que estadísticamente suele venir después en la web. Para convertirlo en asistente hace falta una segunda fase: el **post-entrenamiento**.

El primer paso es el **SFT** (*Supervised Fine-Tuning*, ajuste supervisado), también llamado **ajuste por instrucciones**. Se entrena el modelo con ejemplos de pares instrucción-respuesta de alta calidad, normalmente escritos o revisados por personas. Así aprende el **formato** del diálogo: que ante una pregunta debe dar una respuesta útil, directa y bien estructurada.

El segundo paso es el **aprendizaje de preferencias**, que afina *qué* respuesta es mejor entre varias plausibles. La vía clásica es el **RLHF** (*Reinforcement Learning from Human Feedback*, aprendizaje por refuerzo con retroalimentación humana), ya descrito antes: se entrena un modelo de recompensa a partir de comparaciones humanas y luego se optimiza la política con refuerzo. Es potente, pero complejo y delicado de ajustar.

Por eso ha ganado terreno una alternativa más simple, el **DPO** (*Direct Preference Optimization*, optimización directa de preferencias). En lugar de entrenar un modelo de recompensa aparte y aplicar refuerzo, el DPO reformula el problema como una **única pérdida** que se optimiza directamente sobre pares de respuestas etiquetadas como "preferida" y "rechazada". La idea es ajustar los pesos para que el modelo asigne **más probabilidad** a la respuesta preferida y **menos** a la rechazada, todo con el mismo tipo de entrenamiento supervisado del SFT. El resultado es un proceso más estable y barato, lo que ha popularizado el DPO y sus variantes en modelos abiertos.

### Inferencia y decodificación: por qué generar es caro

Una vez entrenado, el modelo **genera** texto de forma **autorregresiva**: produce un token, lo añade a la secuencia y vuelve a predecir el siguiente, repitiendo el ciclo. Esta naturaleza **secuencial** es la razón de que generar sea inherentemente más lento que procesar una entrada ya completa: cada token depende del anterior y no puede calcularse en paralelo con los que vendrán.

En cada paso, el modelo no entrega un token único, sino una **distribución de probabilidad** sobre todo el vocabulario. Cómo se elige el token a partir de ahí es la **estrategia de decodificación**:

- **Greedy** (codicioso): tomar siempre el token más probable. Es determinista, pero tiende a producir texto repetitivo y plano.
- **Muestreo con temperatura.** La **temperatura** reescala las probabilidades: valores bajos (cercanos a 0) hacen al modelo más conservador y predecible; valores altos, más creativo y arriesgado.
- **Top-k** y **top-p** (*nucleus sampling*). Top-k restringe la elección a los `k` tokens más probables; top-p, a los tokens que acumulan una probabilidad `p` (por ejemplo, 0,9). Ambos descartan la "cola" de opciones absurdas sin renunciar a la variedad.

Una pieza clave del rendimiento es el **KV-cache** (caché de claves y valores). En la atención, cada nuevo token debe atender a todos los anteriores; recalcular en cada paso las representaciones (claves y valores) de todo el historial sería un derroche. El KV-cache las **almacena** y reutiliza, de modo que generar un token nuevo solo requiere calcular su parte. El precio es la **memoria**: el caché crece con la longitud de la secuencia y a menudo es el factor que limita cuántas conversaciones simultáneas caben en una GPU.

Esto introduce la tensión entre **latencia** (cuánto tarda en aparecer la respuesta para un usuario) y **throughput** (cuántos tokens totales por segundo sirve el sistema atendiendo a muchos usuarios a la vez). Procesar peticiones en lotes mejora el throughput, pero puede empeorar la latencia individual; los sistemas de servicio reales buscan un equilibrio entre ambos.

### La ventana de contexto y su coste cuadrático

La **ventana de contexto** es la cantidad máxima de tokens —prompt más respuesta— que el modelo puede tener "a la vista" a la vez. Todo lo que quede fuera, sencillamente, no existe para el modelo.

Ampliarla es difícil por una razón estructural: el coste de la **atención** crece de forma **cuadrática** con la longitud. Si la secuencia se duplica, el cómputo y la memoria de la atención se cuadruplican, porque cada token se compara con todos los demás. Por eso pasar de unos pocos miles de tokens a cientos de miles ha exigido años de investigación en variantes de atención más eficientes, mejores codificaciones de posición y trucos de ingeniería. Hoy existen modelos con ventanas de **cientos de miles**, e incluso del orden de un millón de tokens, pero usar todo ese contexto sigue siendo costoso.

### Cuantización: modelos grandes en hardware modesto

Los pesos de un LLM se almacenan habitualmente en números de coma flotante de 16 bits. La **cuantización** los representa con menos precisión —**int8** (8 bits) o incluso **int4** (4 bits)— reduciendo drásticamente la memoria necesaria. Gracias a ello, modelos que exigirían servidores especializados pueden ejecutarse en un ordenador personal o en una sola GPU de consumo, con una pérdida de calidad por lo general pequeña. Es una de las claves de la explosión de modelos ejecutables localmente.

### Capacidades emergentes y limitaciones

Al crecer en escala, los LLM exhiben **capacidades emergentes**: habilidades —aritmética de varios pasos, razonamiento encadenado, traducción entre idiomas poco vistos— que apenas aparecen en modelos pequeños y surgen de forma relativamente abrupta a partir de cierto tamaño.

Pero la misma maquinaria que los hace versátiles explica su talón de Aquiles: la **alucinación**. Como el modelo optimiza la **plausibilidad** del siguiente token y no la **verdad**, puede generar afirmaciones falsas con total fluidez y confianza, inventando datos, citas o referencias inexistentes. No "sabe" cuándo no sabe. Mitigar esto —con verificación, herramientas externas o recuperación de información, esta última ya tratada— es una de las grandes líneas de trabajo actuales y un recordatorio de que estos sistemas, por impresionantes que sean, tienen límites bien definidos.
