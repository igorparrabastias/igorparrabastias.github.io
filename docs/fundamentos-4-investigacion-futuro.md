# 4 · Investigación reciente y futuro próximo

**Serie _Fundamentos del PLN y la IA_:** [Intro](fundamento-del-pln-y-la-ia.md) · [1 · Orígenes](fundamentos-1-origenes.md) · [2 · Estadística y redes](fundamentos-2-estadistica-redes.md) · [3 · Era LLM](fundamentos-3-era-llm.md) · **4 · Investigación y futuro**

## 📑 Índice

- [🏠 Investigación reciente y futuro próximo (2024–2026)](#-investigación-reciente-y-futuro-próximo-20242026)
    - [👾 Modelos de razonamiento](#-modelos-de-razonamiento)
    - [👾 Mixture of Experts (MoE)](#-mixture-of-experts-moe)
    - [👾 Contexto muy largo](#-contexto-muy-largo)
    - [👾 Eficiencia y modelos pequeños](#-eficiencia-y-modelos-pequeños)
    - [👾 El problema de los datos](#-el-problema-de-los-datos)
    - [👾 Agentes avanzados](#-agentes-avanzados)
- [🏠 El futuro próximo: hacia dónde va](#-el-futuro-próximo-hacia-dónde-va)
    - [👾 Escalado frente a nuevas ideas](#-escalado-frente-a-nuevas-ideas)
    - [👾 El debate sobre la AGI](#-el-debate-sobre-la-agi)
    - [👾 Retos abiertos](#-retos-abiertos)
- [🏠 Conclusión general](#-conclusión-general)

---

## 🏠 Investigación reciente y futuro próximo (2024–2026)

Tras recorrer el camino que va de las primeras ideas estadísticas hasta los grandes modelos de lenguaje, los agentes y la multimodalidad, llegamos al presente: un momento de intensa actividad en el que algunas líneas de investigación parecen especialmente prometedoras. Conviene leer esta sección con cautela: describimos tendencias reales observadas entre 2024 y principios de 2026, pero el campo se mueve deprisa y conviene separar lo que ya funciona de lo que aún es promesa.

### 👾 Modelos de razonamiento

> [!TIP] 😄 Pausa
> Los modelos de razonamiento "piensan más antes de responder". Una virtud que seguimos sin lograr enseñarle a internet.


Una de las novedades más comentadas es la aparición de los llamados **modelos de razonamiento**. La idea central es sencilla de enunciar: en lugar de producir la respuesta de inmediato, el modelo genera primero una **cadena de pensamiento** (*chain-of-thought*), es decir, una secuencia explícita de pasos intermedios antes de dar el resultado final. Lo nuevo no es la cadena de pensamiento en sí —que ya se usaba como técnica de *prompting*—, sino que ahora esa capacidad se **entrena con aprendizaje por refuerzo** (*reinforcement learning*, RL): el modelo recibe recompensa según si llega o no a la solución correcta, y así aprende a razonar de forma más larga y estructurada por su cuenta.

Esto conecta con un segundo concepto clave: el **cómputo en tiempo de inferencia** (*test-time compute*). Tradicionalmente se mejoraba un modelo entrenándolo más; aquí, en cambio, se le permite **"pensar más" al responder**, dedicando más pasos de cálculo a problemas difíciles. Modelos como la serie **o1/o3** de OpenAI y **DeepSeek-R1** mostraron mejoras notables en tareas de matemáticas, programación y lógica precisamente por esta vía. Es un cambio de mentalidad: el rendimiento ya no depende solo del tamaño del modelo, sino también de cuánto se le deja deliberar. Sus límites también son claros: razonar más cuesta más tiempo y dinero, y no garantiza acertar.

### 👾 Mixture of Experts (MoE)

Otra técnica que ha ganado protagonismo es la **mezcla de expertos** (*Mixture of Experts*, MoE). Un modelo MoE es **disperso** (*sparse*): contiene muchos subconjuntos de parámetros llamados *expertos*, pero para cada *token* solo se activa una pequeña fracción de ellos, seleccionada por un componente llamado *router* (enrutador). El resultado es que un modelo puede tener un número total de parámetros muy grande y, sin embargo, gastar en cada predicción solo lo que correspondería a un modelo mucho menor.

La ventaja es de **eficiencia**: permite escalar la capacidad total sin que el coste de cómputo por *token* crezca en la misma proporción. Por eso varios de los modelos más capaces de este periodo emplean arquitecturas MoE. A cambio, son más complejos de entrenar de forma estable y de servir en producción, porque distintos *tokens* activan distintos expertos.

### 👾 Contexto muy largo

El **contexto** —la cantidad de texto que el modelo puede tener "a la vista" a la vez— ha crecido enormemente, pasando de unos pocos miles de *tokens* a cientos de miles e incluso **millones**. Esto abre usos prácticos: analizar libros enteros, bases de código completas o grandes colecciones de documentos sin trocearlos.

Sin embargo, hay matices importantes. Que un modelo *acepte* un contexto enorme no significa que lo *aproveche* perfectamente: se ha observado el fenómeno de la información perdida "en medio" del texto, donde los datos situados en la zona central reciben menos atención efectiva. Además, el coste de procesamiento crece con la longitud. Por eso el contexto largo no sustituye del todo a técnicas como la **generación aumentada por recuperación** (*Retrieval-Augmented Generation*, RAG), ya presentada, sino que la complementa.

### 👾 Eficiencia y modelos pequeños

En paralelo a la carrera por modelos cada vez mayores, ha surgido una tendencia igual de relevante: **modelos pequeños sorprendentemente capaces**. Mediante mejores datos y técnicas como la **destilación** —entrenar un modelo pequeño (*estudiante*) para imitar a uno grande (*maestro*)—, se han logrado modelos compactos que rinden muy por encima de lo que su tamaño sugeriría.

Esto habilita la ejecución **en el dispositivo** (*on-device*): modelos que corren en teléfonos u ordenadores personales sin enviar datos a la nube, con ventajas en privacidad, latencia y coste. La eficiencia, en suma, se ha vuelto un objetivo de investigación tan legítimo como la capacidad bruta.

### 👾 El problema de los datos

Las leyes de escala, ya explicadas, asumían abundancia de datos de calidad. Pero el **texto web de alta calidad es finito** y hay señales de que las mejores fuentes se están agotando. Esto ha vuelto central la cuestión de los datos.

Una respuesta son los **datos sintéticos**: texto generado por los propios modelos para entrenar a otros. Usados con cuidado —por ejemplo, en dominios verificables como las matemáticas— resultan valiosos; usados sin filtro, corren el riesgo de degradar el modelo al realimentar sus propios errores. De ahí que el **filtrado y la curación de datos de calidad** se hayan convertido en una disciplina por derecho propio: a menudo importa más la calidad y diversidad de los datos que su mera cantidad.

### 👾 Agentes avanzados

Por último, el concepto de **agente** ya tratado se ha materializado en sistemas más capaces, incluido el llamado *computer use* (uso del ordenador), en el que el modelo opera un navegador o una interfaz como lo haría una persona. Lo señalamos aquí solo para subrayar que sigue siendo un área en rápida evolución, todavía frágil en fiabilidad.

## 🏠 El futuro próximo: hacia dónde va

### 👾 Escalado frente a nuevas ideas

El debate de fondo del campo puede resumirse en una pregunta: **¿basta con más cómputo y más datos, o hacen falta avances arquitectónicos nuevos?** Una postura, apoyada en el éxito histórico de las leyes de escala, sostiene que seguir aumentando recursos seguirá dando frutos. Otra advierte que se aprecian **rendimientos decrecientes** y límites de datos, y que los próximos saltos vendrán de ideas distintas —como los propios modelos de razonamiento, que mejoran sin agrandar el modelo base.

La realidad observada hasta principios de 2026 sugiere que **ambas cosas conviven**: el escalado sigue ayudando, pero las innovaciones en cómo se entrena y se usa el cómputo (RL sobre razonamiento, *test-time compute*, MoE) están aportando mejoras que el simple tamaño no daba. No hay consenso, y es honesto reconocerlo.

### 👾 El debate sobre la AGI

Pocos términos generan más discusión que **inteligencia artificial general** (*Artificial General Intelligence*, AGI), entendida a grandes rasgos como una IA con capacidad cognitiva comparable a la humana en una amplia gama de tareas. Algunas voces de la industria afirman que está cerca; otras, igual de informadas, lo consideran lejano o mal definido.

Conviene la prudencia. Primero, **no existe una definición única ni una prueba acordada** de qué contaría como AGI. Segundo, los modelos actuales muestran capacidades impresionantes y, a la vez, fallos elementales que una inteligencia general no cometería. Tercero, buena parte de las afirmaciones más rotundas proceden de actores con intereses comerciales. Lo riguroso es decir que **hay progreso real y también incertidumbre real**, y que afirmar fechas concretas es, hoy, especulación más que hecho.

### 👾 Retos abiertos

Más allá de la capacidad, persisten problemas serios que condicionarán el futuro:

- **Fiabilidad y alucinación**: los modelos aún generan información falsa con tono convincente. Reducir esto es requisito para usos críticos.
- **Alineación y seguridad**: asegurar que sistemas cada vez más autónomos actúen conforme a los valores e intenciones humanas es un problema técnico y social no resuelto, y más urgente cuanto más capaces y agénticos son los modelos.
- **Energía y sostenibilidad**: entrenar y servir grandes modelos consume mucha electricidad y agua; la eficiencia no es solo económica, también ambiental.
- **Concentración de cómputo y poder**: la capacidad de entrenar modelos punteros está en pocas manos, lo que plantea cuestiones de dependencia, competencia y gobernanza.
- **Regulación**: marcos como el Reglamento de IA de la Unión Europea buscan equilibrar innovación y derechos; el reto es regular una tecnología que cambia más rápido que las leyes.
- **Impacto en el empleo y la sociedad**: la automatización de tareas cognitivas plantea transformaciones laborales cuya magnitud y velocidad aún no se conocen con certeza.

Ninguno de estos retos tiene solución cerrada. Forman parte, precisamente, de lo que hace de este un momento abierto.

## 🏠 Conclusión general

Hemos recorrido un arco de más de setenta años, desde los planteamientos de mediados del siglo XX hasta los sistemas de hoy. Si algo lo unifica, es una sola pregunta persistente: **cómo representar y procesar el significado del lenguaje en una máquina**.

La respuesta ha cambiado muchas veces. Empezó con **técnicas estadísticas** que contaban palabras y modelaban probabilidades, y con métodos de **reducción dimensional** que buscaban estructura en grandes matrices de texto. Siguió con los **embeddings**, que dieron a las palabras una representación numérica donde la cercanía geométrica capturaba parecido de significado. Llegó el **Transformer**, cuyo mecanismo de atención permitió modelar el contexto de forma flexible y escalable, y con él los **grandes modelos de lenguaje**, que convirtieron la predicción del siguiente *token* en una capacidad asombrosamente general. Y desemboca en los **agentes multimodales**, sistemas que razonan, usan herramientas y combinan texto, imagen y más.

Es un logro notable. Tareas que parecían exclusivamente humanas —redactar, traducir, programar, resumir, conversar— hoy se asisten o automatizan con calidad antes impensable. Pero sería deshonesto cerrar con triunfalismo. Estos sistemas **no comprenden como nosotros**: alucinan, fallan en lo elemental, dependen de enormes recursos y plantean problemas de fiabilidad, alineación, energía y poder que no están resueltos. La distancia entre *imitar el lenguaje con maestría* y *entender el mundo* sigue siendo objeto de debate legítimo.

Quizá esa sea la mejor manera de despedir este recorrido: con **asombro y prudencia a partes iguales**. Hemos avanzado muchísimo y, a la vez, las preguntas centrales —qué es comprender, qué es razonar, hasta dónde llegará todo esto— siguen abiertas. La historia que cuenta este documento no tiene final escrito. Apenas estamos en uno de sus capítulos, y los siguientes los escribirán, en parte, quienes hoy se molestan en entender de verdad cómo funciona todo esto.
