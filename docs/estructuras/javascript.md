# Estructuras de datos en JavaScript

Esta página es la versión **JavaScript** del curso de estructuras de datos del sitio: el mismo concepto que ya viste como notebooks de Python, pero ahora implementado con clases de JS. La idea es comparar — *el mismo concepto, otra implementación* — para que veas que las ideas (nodos, punteros, complejidad) son universales aunque la sintaxis cambie.

Todo el código que aparece embebido a continuación es **código real** del laboratorio, leído directamente desde `learning/computer-science-basics/data-structures/`. Si tocas el archivo fuente, esta página se actualiza sola.

> [!TIP]
> Mientras lees, pregúntate "¿qué pasa cuando hay un millón de elementos?". Esa pregunta es, básicamente, todo el análisis de complejidad resumido en una frase. 🧠

---

## Array (arreglo)

El **array** es la estructura más básica: una secuencia indexada de elementos en memoria contigua. En JavaScript el array nativo (`[]`) ya viene de fábrica y es enormemente flexible (puede crecer, mezclar tipos, etc.).

| Operación | Complejidad |
|-----------|-------------|
| Acceso por índice `arr[i]` | O(1) |
| Búsqueda lineal | O(n) |
| `push` / `pop` (al final) | O(1) amortizado |
| `shift` / `unshift` (al inicio) | O(n) — hay que reindexar todo |

Casi todas las demás estructuras de esta página se construyen *encima* del array o de objetos. Por eso es el punto de partida natural, igual que en la pista de Python.

---

## Lista enlazada (LinkedList)

Una **lista enlazada** encadena nodos, donde cada nodo guarda un valor (`element`) y un puntero al siguiente (`next`). A diferencia del array, los elementos **no** están contiguos en memoria: para llegar al elemento `i` hay que recorrer la cadena desde la cabeza (`head`).

- **Insertar/eliminar al principio**: O(1) — solo se reconectan punteros.
- **Acceder/buscar por posición**: O(n) — no hay acceso aleatorio.

```javascript
--8<-- "learning/computer-science-basics/data-structures/LinkedList.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/LinkedList.js)

---

## Pila (Stack)

La **pila** sigue la política **LIFO** (*Last In, First Out*): el último en entrar es el primero en salir, como una pila de platos. Aquí se implementa apoyándose en el array nativo (`push`/`pop`).

- `push`, `pop`, `peek`, `isEmpty`: todas O(1).
- Usos típicos: deshacer/rehacer, evaluación de expresiones, gestión de la pila de llamadas (¡la recursión usa una pila por debajo!).

```javascript
--8<-- "learning/computer-science-basics/data-structures/Stack.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/Stack.js)

---

## Cola (Queue)

La **cola** sigue la política **FIFO** (*First In, First Out*): el primero en llegar es el primero en salir, como la fila del supermercado. Se implementa con `push` (enqueue) y `shift` (dequeue).

- `enqueue`, `front`, `isEmpty`: O(1). `dequeue` con `shift` es O(n) en arrays nativos (reindexa), un detalle a tener en cuenta en producción.
- El archivo incluye una aplicación didáctica: `generatePrintBinary`, que genera números binarios con una cola haciendo un BFS implícito de un árbol.

```javascript
--8<-- "learning/computer-science-basics/data-structures/Queue.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/Queue.js)

---

## Grafo (Graph)

Un **grafo** modela relaciones: vértices conectados por aristas. Esta implementación usa **lista de adyacencia** (un `Map` de vértice → vecinos) y es no dirigida (cada arista se añade en ambos sentidos).

Incluye los dos recorridos clásicos:

- **BFS** (Breadth First Search): explora por niveles usando una **cola**. O(V + E).
- **DFS** (Depth First Search): explora en profundidad de forma recursiva (usando la **pila** de llamadas). O(V + E).

Fíjate cómo el grafo reutiliza la `Queue` para el BFS: las estructuras se apoyan unas en otras.

```javascript
--8<-- "learning/computer-science-basics/data-structures/Graph.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/Graph.js)

---

## Tabla hash (HashTable)

Una **tabla hash** asocia claves a valores calculando, con una *función hash*, en qué "cubeta" (bucket) guardar cada par. Es la estructura que da O(1) promedio a inserción y búsqueda, y es justo lo que usan por dentro los objetos `{}` de JavaScript.

El archivo muestra **dos implementaciones** para comparar:

- `HashTableObject`: usa un objeto `{}` como almacén.
- `HashTableArray`: usa un array de buckets con encadenamiento (cada bucket es una lista de pares `[clave, valor]`), que es como se resuelven las **colisiones**.

- Inserción/búsqueda: **O(1) promedio**, O(n) en el peor caso (muchas colisiones).

```javascript
--8<-- "learning/computer-science-basics/data-structures/HashTable.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/HashTable.js)

---

## Montículo (Heap)

Un **heap** (montículo binario) es un árbol binario *casi completo* que mantiene la **propiedad de heap**: en un *min-heap* cada padre es menor o igual que sus hijos (en un *max-heap*, mayor o igual). Es la base de las **colas de prioridad** y del algoritmo *Heapsort*.

- Insertar y extraer el mínimo/máximo: **O(log n)**.
- Consultar el mínimo/máximo (la raíz): **O(1)**.

> [!NOTE]
> En el laboratorio el archivo `Heap.js` está reservado como ejercicio (todavía vacío). Aquí lo dejamos documentado conceptualmente; en la pista de Python encontrarás el heap implementado y ejecutable como notebook. *El mismo concepto, otra implementación.*

---

## Árbol binario de búsqueda (BinarySearchTree)

Un **árbol binario de búsqueda** (BST) mantiene en cada nodo el invariante: todo lo de la izquierda es menor y todo lo de la derecha es mayor. Eso permite buscar, insertar y borrar en **O(log n)** *si el árbol está equilibrado* (y O(n) si degenera en una "lista").

Esta implementación es bastante completa e incluye:

- `insert` / `remove` (con los tres casos de borrado: hoja, un hijo, dos hijos).
- Recorridos **inorder** (devuelve los datos ordenados), **preorder** y **postorder**.
- `traverseBFS` (recorrido por niveles), `getMin` / `getMax`.
- Funciones sueltas `isBalanced` y `height` para comprobar si el árbol está equilibrado.

```javascript
--8<-- "learning/computer-science-basics/data-structures/BinarySearchTree.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/data-structures/BinarySearchTree.js)

---

## ¿Y ahora qué?

Estas estructuras son los ladrillos. En la página de [Algoritmos en JavaScript](../algoritmos/javascript.md) las pondremos a trabajar: búsqueda binaria, ordenamientos, Dijkstra sobre grafos, programación dinámica y más. Y en [Problemas resueltos](../algoritmos/problemas-javascript.md) verás cómo se combinan para resolver retos tipo entrevista.
