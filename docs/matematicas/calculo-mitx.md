# Cálculo 1A (MITx / UTAustinX) — por qué las mates sostienen los algoritmos

**[Calculus 1A: Differentiation](https://www.edx.org/learn/calculus/the-university-of-texas-at-austin-calculus-1a-differentiation)** (código Calc001x en edX), un curso de cálculo diferencial elaborado conjuntamente por el **MIT** y **UTAustinX**. Es el primer ladrillo de una serie que recorre derivadas, integrales y series.

> [!NOTE]
> 🔵 Material de terceros. El curso y sus *slides* son del MIT/UTAustinX; aquí solo describo qué cubre y por qué importa. **No reproduzco los PDFs.**
>
> Crédito: **MITx / UTAustinX**. Curso original: **[Calculus 1A: Differentiation en edX](https://www.edx.org/learn/calculus/the-university-of-texas-at-austin-calculus-1a-differentiation)**.

## Qué cubre

En mi copia conservo las *slides* de los temas iniciales y una **chuleta de cálculo** completa como material de referencia. El curso, en su recorrido, trata:

- **Funciones**: cómo describirlas, leerlas y representarlas; funciones polinómicas y sus gráficas.
- **Límites y continuidad**: la maquinaria que da sentido a "acercarse infinitamente".
- **La derivada**: definición como límite, interpretación geométrica (pendiente de la tangente) y como **tasa de cambio**.
- **Reglas de derivación**: producto, cociente, cadena; derivadas de polinomios, trigonométricas, exponenciales y logarítmicas.
- **Aplicaciones**: optimización (máximos y mínimos), linealización y aproximación.

## Por qué las mates importan para los algoritmos

No es matemática por deporte: es la base sobre la que se apoyan media docena de ideas que aparecen una y otra vez en programación y ciencia de datos.

- **Optimización y descenso de gradiente**: entrenar casi cualquier modelo de *machine learning* es minimizar una función de coste. El **gradiente** (derivadas parciales) es la brújula que indica hacia dónde bajar. Sin derivadas no hay *backpropagation*.
- **Análisis de complejidad**: razonar sobre cómo crece el coste de un algoritmo (la notación *Big-O*) es, en el fondo, razonar sobre **tasas de crecimiento** de funciones, justo el lenguaje del cálculo.
- **Tasas de cambio**: muchísimos problemas (físicos, económicos, de simulación) se modelan con derivadas; entender la derivada es entender el cambio.
- **Aproximación**: linealizar una función cerca de un punto es la idea detrás de métodos numéricos como Newton-Raphson, omnipresentes cuando no hay solución cerrada.

> [!TIP]
> Conecta con el resto del sitio: lo que aquí es teoría se vuelve práctica en la sección de [Matemáticas y teoría](../index.md) y en los *problem sets* de [6.00.2x](../practica/mitx-6002x.md), donde la optimización (vacas espaciales incluidas 🐄🚀) deja de ser abstracta. Entender de dónde sale un gradiente convierte muchas "recetas mágicas" del ML en algo que de verdad se comprende.
