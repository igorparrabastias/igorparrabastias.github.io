# Estructuras de datos

Cómo guardamos los datos para poder trabajar con ellos: ordenados, desordenados o
jerárquicos. Aquí van desde las estructuras **nativas de Python** hasta implementaciones
**propias** (las que hay debajo del capó), y el mismo concepto visto en **otro lenguaje**.

> [!TIP]
> Elegir bien la estructura es la mitad de la solución. La otra mitad es el
> [algoritmo](../algoritmos/index.md) que la recorre. 🧩

## Recorridos disponibles

<div class="grid cards" markdown>

-   :material-language-python: __En Python (notebooks ejecutables)__

    ---

    Estructuras nativas (listas, tuplas, dicts, sets), implementación propia de listas
    enlazadas, pilas y colas, **tablas hash**, **heaps** y estructuras avanzadas.
    En el menú lateral, bajo esta sección.

-   :material-language-javascript: __En JavaScript__

    ---

    Las mismas estructuras (lista, pila, cola, grafo, hash, heap, BST) implementadas en JS
    con tests. *El mismo concepto, otra implementación.*

    [:octicons-arrow-right-24: Ver](javascript.md)

-   :material-file-tree: __Estructuras de árboles__

    ---

    Árboles fundamentales, balanceados (AVL, rojo-negro, splay) y de búsqueda en disco
    (B, B+), con sus implementaciones.

    [:octicons-arrow-right-24: Ver índice](../index-trees.md)

</div>

## El mapa mental

| Familia | Para qué brilla | Dónde |
|---|---|---|
| Listas / arreglos | acceso por índice, orden | Python · JS |
| Pilas y colas | LIFO / FIFO, recorridos | Python · JS |
| Tablas hash | búsqueda O(1) promedio | Python · JS |
| Heaps | prioridad, top-k | Python · JS |
| Árboles | jerarquía, búsqueda ordenada | Python (sección árboles) |
| Grafos | relaciones, redes | ver [Algoritmos](../algoritmos/index.md) |

> [!NOTE]
> Cada notebook trae botón **"Abrir en Colab"** para ejecutarlo en el navegador.
