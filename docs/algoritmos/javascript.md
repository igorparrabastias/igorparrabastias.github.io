# Algoritmos en JavaScript

Esta página es la pista **JavaScript** del curso de algoritmos del sitio. Cada tema que aquí ves implementado en JS existe también como notebook de Python en otra parte del sitio: *el mismo concepto, otra implementación*. La gracia es comparar las ideas — divide y vencerás, recursión, memoización — más allá del lenguaje.

Todo el código embebido es **real**, leído desde `learning/computer-science-basics/data-structures/`. Si te falta el contexto de las estructuras (pila, cola, grafo…), pásate primero por [Estructuras de datos en JavaScript](../estructuras/javascript.md).

> [!TIP]
> Ordenar parece aburrido hasta que descubres que hay como diez maneras de hacerlo y todas pelean por ser "la mejor". Spoiler: no hay una mejor, hay una mejor *para cada caso*. ⚔️

---

## Búsqueda binaria (Binary Search)

La **búsqueda binaria** encuentra un elemento en un array **ordenado** partiendo el rango por la mitad en cada paso: O(log n). El archivo trae tres variantes para que compares estilos:

- `binarySearchIterative` y `binarySearchIterative2`: versiones iterativas, **O(1)** de espacio.
- `binarySearchRecursive`: versión recursiva, **O(log n)** de espacio (por la pila de llamadas).

> [!WARNING]
> Requiere que el array **ya esté ordenado**. Si no lo está, primero ordena (ver abajo) y luego busca — o la respuesta será basura.

```javascript
--8<-- "learning/computer-science-basics/data-structures/BinarySearch.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/BinarySearch.js)

---

## Ordenamientos

Cuatro algoritmos clásicos, de menor a mayor sofisticación. Resumen para tener a mano:

| Algoritmo | Mejor | Promedio | Peor | Espacio | ¿In-place? | ¿Estable? |
|-----------|:-----:|:--------:|:----:|:-------:|:----------:|:---------:|
| Bubble    | O(n)  | O(n²)    | O(n²)| O(1)    | Sí | Sí |
| Insertion | O(n)  | O(n²)    | O(n²)| O(1)    | Sí | Sí |
| Merge     | O(n log n) | O(n log n) | O(n log n) | O(n) | No | Sí |
| Quick     | O(n log n) | O(n log n) | O(n²) | O(log n) | Sí | No |

### Bubble Sort

El **bubble sort** compara pares de elementos adyacentes y los intercambia si están desordenados, repitiendo hasta que no haya más intercambios. Los valores grandes "se hunden" y los pequeños "burbujean" hacia arriba — de ahí el nombre.

Es el más simple de escribir y entender, ordena **in-place** (poca memoria extra) y es **estable**. Su gran defecto es la velocidad: el tiempo crece casi exponencialmente con el número de elementos (diez veces más datos ≈ cien veces más tiempo). Mejor caso O(n) si el array ya está ordenado; peor y promedio O(n²). Resérvalo para arrays pequeños (unos pocos cientos de elementos).

```javascript
--8<-- "learning/computer-science-basics/data-structures/bubbleSort.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/bubbleSort.js)

### Insertion Sort

El **insertion sort** funciona como cuando ordenas cartas en la mano: divide el array en una parte ordenada y otra sin ordenar, y va tomando elementos de la parte desordenada para insertarlos en su sitio dentro de la ordenada.

Es **adaptativo**: si los datos ya están casi ordenados, roza O(n). Es simple, **estable**, in-place (O(1) extra) y muy eficiente para **pocos elementos** o arrays casi ordenados. Su límite es el promedio O(n²), que lo hace lento frente a merge o quicksort cuando hay muchos datos.

```javascript
--8<-- "learning/computer-science-basics/data-structures/insertionSort.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/insertionSort.js)

### Merge Sort

El **merge sort** aplica **divide y vencerás**: parte el array en dos mitades, las ordena recursivamente y luego las **mezcla** (`merge`) en orden. Son dos funciones: `mergeSort` (parte) y `merge` (combina).

Su tiempo es **O(n log n)** en todos los casos — uno de los más rápidos y predecibles. El precio: **no es in-place**, necesita O(n) de espacio auxiliar para los subarreglos. Se presta genial a multihilo (cada mitad se ordena por separado) y es el favorito para ordenar **listas enlazadas**, donde el merge se hace sin coste extra de memoria.

```javascript
--8<-- "learning/computer-science-basics/data-structures/mergeSort.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/mergeSort.js)

### Quick Sort

El **quicksort** también es divide y vencerás, pero **in-place**: elige un *pivote*, coloca a su izquierda lo menor y a su derecha lo mayor (`partition`), y repite recursivamente sobre cada lado.

Promedio **O(n log n)**; peor caso O(n²) si eliges sistemáticamente el peor pivote (por eso en la práctica se usa pivote aleatorio). Suele ser el preferido para **arrays** porque no gasta memoria extra y aprovecha bien la *localidad de caché*. Curiosidad: el `sort()` nativo de JavaScript usa por dentro insertion sort (V8/Chrome) o merge sort (Firefox/Safari) según el motor.

> [!NOTE]
> Regla mnemotécnica: **Quick** para arrays (in-place, cache-friendly), **Merge** para listas enlazadas (mezcla sin coste extra).

```javascript
--8<-- "learning/computer-science-basics/data-structures/quickSort.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/quickSort.js)

---

## Dijkstra — camino más corto

El algoritmo de **Dijkstra** encuentra el camino de menor coste desde un nodo origen al resto, en grafos con pesos no negativos. Mantiene las distancias mínimas conocidas y va "visitando" siempre el nodo no visitado más cercano.

El laboratorio incluye **dos implementaciones** sobre grafos representados como objetos:

- `dijkstra-shortest-path.js`: devuelve `{ distance, path }` reconstruyendo el camino con un mapa de `parents`.
- `dijkstra-shortest-path2.js`: construye una tabla de costes (`vertex`, `cost`) e imprime tanto la tabla como el camino trazado.

```javascript
--8<-- "learning/computer-science-basics/data-structures/dijkstra-shortest-path.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/dijkstra-shortest-path.js)

```javascript
--8<-- "learning/computer-science-basics/data-structures/dijkstra-shortest-path2.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/dijkstra-shortest-path2.js)

---

## Programación dinámica (Dynamic Programming)

La **programación dinámica** resuelve problemas que tienen **subproblemas solapados** y **subestructura óptima**: se descomponen en subproblemas más pequeños cuyas soluciones se reutilizan. El archivo lo ilustra con Fibonacci en sus dos sabores:

- **Top-down con memoización** (`fibWithMemo`): recursión que guarda en un `memo` los resultados ya calculados para no repetirlos. Elegante, pero gasta memoria y pila.
- **Bottom-up con tabulación** (`fibWithTab`): iterativo, rellena una tabla desde el caso base hacia arriba. Mismo tiempo, **mejor espacio**, sin recursión.

```javascript
--8<-- "learning/computer-science-basics/data-structures/DynamicProgramming.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/DynamicProgramming.js)

---

## Recursión (Recursion)

Una función **recursiva** se llama a sí misma con un problema más pequeño, hasta llegar a un **caso base** que la detiene. El archivo muestra tres ejemplos canónicos: `countDown` (cuenta atrás), `factorial` (factorial) y `fibonacci` (la versión *sin* memoización — útil para ver, por contraste, por qué la programación dinámica de arriba es tan necesaria).

> [!TIP]
> Toda recursión necesita un caso base, o tu programa se cae con un *"Maximum call stack size exceeded"*. La recursión sin caso base es como una conversación que nunca termina. 🔁

```javascript
--8<-- "learning/computer-science-basics/data-structures/Recursion.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/Recursion.js)

---

## Backtracking

El **backtracking** ("vuelta atrás") explora sistemáticamente todas las soluciones candidatas construyéndolas paso a paso, y **deshace** ("retrocede") la última decisión en cuanto detecta que un camino no lleva a una solución válida. Es recursión + poda.

> [!NOTE]
> En el laboratorio el archivo `Backtracing.js` está reservado como ejercicio (todavía vacío). Pero tienes un ejemplo de backtracking **real y funcionando** en los problemas resueltos: `combinationSum` añade un número, recursa, y si no llega a la suma deshace el último paso (`temp.splice(...)`). Lo ves en detalle en [Problemas resueltos en JavaScript](problemas-javascript.md#strings-y-backtracking).

---

## Siguiente paso

Lleva todo esto a la práctica en [Problemas resueltos en JavaScript](problemas-javascript.md): retos tipo entrevista agrupados por tema (arrays, árboles, grafos, strings y backtracking), cada uno con su solución embebida y sus tests.
