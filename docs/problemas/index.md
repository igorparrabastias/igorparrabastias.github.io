# Problemas de Estructuras de Datos y Algoritmos

Problemas clásicos de entrevista y competición, **resueltos paso a paso en Python**: enunciado, idea del algoritmo, análisis de complejidad y código con ejemplos. Cada enlace abre el notebook renderizado en el sitio (y se puede abrir en Colab).

> [!TIP]
> Aquí se aplica todo lo demás: las [estructuras de datos](../estructuras/index.md) (arrays, listas enlazadas, árboles) y los [algoritmos](../algoritmos/index.md) (hashing, recursión, dos punteros). Si un problema se atasca, suele faltar elegir la estructura adecuada. 🧩

## Arrays y hashing

### [Two Sum — ¿existe el par con la suma dada?](../notebook/problemas-de-estructuras-y-algoritmos/two-sum.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/two-sum.svg" alt="Array recorrido guardando lo visto; al llegar al 7 se busca su pareja 9−7=2, que ya estaba guardada" width="460"></p>

Dado un array y un objetivo, encontrar dos números que sumen ese objetivo. Técnica: **hashing** · O(N) tiempo, O(N) espacio.

### [Subconjunto contiguo de suma más grande](../notebook/problemas-de-estructuras-y-algoritmos/largest-sum-contiguous-subarray.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/largest-sum-contiguous-subarray.svg" alt="Fila de números con el tramo contiguo 3, 4, −1, 5 resaltado, cuya suma 11 es la máxima" width="460"></p>

El subarreglo contiguo con la suma máxima. Algoritmo de **Kadane** · O(N) tiempo, O(1) espacio.

## Matemáticas

### [Máximo Común Divisor (GCD)](../notebook/problemas-de-estructuras-y-algoritmos/greatest-common-divisor.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/greatest-common-divisor.svg" alt="Cadena de divisiones de Euclides: 48÷18 deja 12, 18÷12 deja 6, 12÷6 deja 0; el MCD es 6" width="460"></p>

El mayor número que divide a dos enteros sin residuo. **Algoritmo de Euclides** · O(log(min(a, b))) tiempo, O(1) espacio.

## Búsqueda en matrices

### [Buscar en una matriz ordenada por filas y columnas](../notebook/problemas-de-estructuras-y-algoritmos/search-in-a-row-wise-and-column-wise-sorted-matrix.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/search-in-a-row-wise-and-column-wise-sorted-matrix.svg" alt="Matriz 4x4 ordenada; partiendo de la esquina superior derecha se avanza a la izquierda o hacia abajo hasta hallar el 29" width="460"></p>

Localizar un elemento aprovechando el orden por filas **y** columnas. **Búsqueda por eliminación** · O(n + m) tiempo, O(1) espacio.

## Listas enlazadas

### [Invertir una lista enlazada en grupos de tamaño k](../notebook/problemas-de-estructuras-y-algoritmos/reverse-nodes-in-k-group.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/reverse-nodes-in-k-group.svg" alt="Lista enlazada 1→2→3→4 que, invirtiendo de a grupos de k=2, queda 2→1→4→3" width="460"></p>

Invertir los nodos de a grupos de tamaño dado. **Inversión por grupos** · O(n) tiempo, O(1) espacio.

## Árboles binarios

### [Reconstruir el árbol binario desde preorden e inorden](../notebook/problemas-de-estructuras-y-algoritmos/construct-binary-tree-from-preorder-and-inorder-traversal.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/construct-binary-tree-from-preorder-and-inorder-traversal.svg" alt="El primer elemento del preorden (3) es la raíz; en el inorden lo de su izquierda y derecha forma los subárboles" width="460"></p>

Dados los recorridos en preorden e inorden, reconstruir el árbol. **Reconstrucción recursiva** · O(n) tiempo, O(n) espacio.

### [Suma máxima de rutas en un árbol binario](../notebook/problemas-de-estructuras-y-algoritmos/maximum-path-sum-in-a-binary-tree.ipynb)

<p align="center"><img src="../assets/img/problemas/svg/maximum-path-sum-in-a-binary-tree.svg" alt="Árbol binario con la ruta 15–20–7 resaltada, cuya suma 42 es la máxima" width="460"></p>

La ruta de suma máxima entre dos nodos cualesquiera. **Recursión con manejo de estados** · O(N) tiempo, O(H) espacio.
