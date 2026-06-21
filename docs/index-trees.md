:arrow_backward: [Indice](index.md)

# :file_folder: Árboles Y Algoritmos de Operaciones

Seguiremos un orden que asegura una progresión lógica, desde lo más **fundamental** a lo más **avanzado**, permitiendo construir una base sólida antes de abordar estructuras más complejas.  

<details>
  <summary>Tips</summary>
  
- :file_folder: Repása esta página de principio a fin para tener una visión global sobre la **estructura de datos** de tipo **árbol**.  
- :ledger: Después de eso sigue cada link en el primer nivel  en forma secuencial para aprender sobre cada tipo.   
- :page_with_curl: Y al final, una vez hayas revisado todos los tipos, avanza a los link anidados para profundizar más, teniendo ya muy claro el contexto general.
</details>

## Fundamentales

Entre ellos, los **árboles binarios** son aquellos en los que cada nodo tiene como máximo dos hijos, lo que facilita la implementación y manipulación de datos. Por otro lado, los **árboles de búsqueda binaria** son una variante especializada en la que cada nodo cumple con una regla de ordenamiento, permitiendo búsquedas eficientes y rápidas en conjuntos de datos ordenados. Estas estructuras son esenciales en la programación y la gestión de datos, siendo ampliamente utilizadas en aplicaciones como bases de datos, algoritmos de búsqueda y optimización.

- :ledger: [Arboles](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/introduccion.ipynb) Introducción general a árboles. Terminología y consideraciones de implementación.
  - :page_with_curl: [Tipos de Árboles](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/tipos-de-arboles.ipynb) Tipos principales y su categorización según su estructura y propósito.
  - :page_with_curl: [Algoritmos Relacionados con Árboles](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/algoritmos-relacionados-con-arboles.ipynb)
  - :page_with_curl: [Ejemplo de Algoritmo en Sistemas de Recomendación](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/ejemplo-de-algoritmo-en-sistemas-de-recomendacion.ipynb)
  - :page_with_curl: [Ejemplo de Algoritmo par Procesamiento del Lenguaje Natural](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/ejemplo-de-algoritmo-par-procesamiento-del-lenguaje-natural.ipynb)
  - :page_with_curl: [Ejemplo de Algoritmo en Bioinformática](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/ejemplo-de-algoritmo-en-bioinformatica.ipynb)
  - **Implementación de `Tree`**
    - :page_with_curl: [Implementación Básica de Arbol](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/tree-elemental.ipynb)  
    - :floppy_disk: [Tree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/Tree.py)
  <!-- - :page_with_curl: [Ejercicios](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/ejercicios.ipynb)   -->

- :ledger: [Árboles Binarios](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-binario.ipynb) Concepto básico y recorridos.
  - :page_with_curl: [Aplicaciones de Árboles Binarios](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-binarios.ipynb)
  - :page_with_curl: [Consideraciones al Implementar un Arbol Binario](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-un-arbol-binario.ipynb)
  - **Implementación de `BinaryTree`**
    - :page_with_curl: [Inserción manual](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/insercion-manual.ipynb)  
    - :page_with_curl: [Inserción automática](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/insercion-automatica.ipynb)  
    - :page_with_curl: [Búsqueda recursiva](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/busqueda-recursiva.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/eliminacion-de-nodos.ipynb) 
    - :floppy_disk: [BinaryTree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/BinaryTree.py) 
  - **Métodos de Recorrido**
    - :page_with_curl: [preorder (DFS)](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-preorder.ipynb)
    - :page_with_curl: [inorder (DFS)](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-inorder.ipynb)
    - :page_with_curl: [postorder (DFS)](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-postorder.ipynb)
    - :page_with_curl: [level_order (BFS)](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-level_order.ipynb)
  - **Métodos de Utilidad**
    - :page_with_curl: [height](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-height.ipynb)
    - :page_with_curl: [size](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-size.ipynb)
    - :page_with_curl: [is_balanced](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-is_balanced.ipynb)
  - **Métodos Avanzados**
    - :page_with_curl: [mirror](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-mirror.ipynb)
    - :page_with_curl: [is_tree](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-is_tree.ipynb)
    - :page_with_curl: [convert_to_linked_list](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-convert_to_linked_list.ipynb)
    - :page_with_curl: [serialize_deserialize](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-serialize_deserialize.ipynb)

- :ledger: [Árboles Binarios de Búsqueda (BST)](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-binario-de-busqueda-bst.ipynb)  Evolución del árbol binario, introduce la idea de ordenamiento y eficiencia en la búsqueda.
  - :page_with_curl: [Aplicaciones de Árboles Binarios de Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-binarios-de-busqueda.ipynb)
  - :page_with_curl: [Consideraciones al Implementar Métodos para BST](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-metodos-para-bst.ipynb)
  - **Implementación de `BST`**
    - :page_with_curl: [Inserción](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/bst-insercion.ipynb)  
    - :page_with_curl: [Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/bst-busqueda.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/bst-eliminacion-de-nodos.ipynb)  
    - :floppy_disk: [BST.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/BST.py) 
  - **Métodos de Utilidad**
    - :page_with_curl: [get_successor](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-get_successor.ipynb)
    - :page_with_curl: [get_predecessor](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-get_predecessor.ipynb)
    - :page_with_curl: [lowest_common_ancestor](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-lowest_common_ancestor.ipynb)
  - **Métodos Avanzados**
    - :page_with_curl: [is_bst](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-is_bst.ipynb)
    - :page_with_curl: [is_subtree](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-is_subtree.ipynb)
    - :page_with_curl: [find_level](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-find_level.ipynb)
    - :page_with_curl: [bst_convert_to_linked_list](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-bst_convert_to_linked_list.ipynb)
    - :page_with_curl: [bst_serialize_deserialize](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/implementacion-bst_serialize_deserialize.ipynb)

Los árboles **AVL**, **rojo-negro** y **splay** son variantes avanzadas de los **árboles binarios de búsqueda**, diseñadas para mejorar el rendimiento en operaciones de inserción, eliminación y búsqueda. Los **árboles AVL** mantienen un equilibrio óptimo, asegurando que la diferencia de altura entre subárboles no supere un valor específico, lo que garantiza tiempos de búsqueda consistentes. Los **árboles rojo-negro**, por otro lado, aplican reglas de coloración para mantener un equilibrio relajado, lo que los hace más eficientes en operaciones de inserción y eliminación. Mientras tanto, los **árboles splay** utilizan rotaciones y reorganizaciones dinámicas para llevar a los nodos más accesibles a la raíz, optimizando las operaciones de búsqueda. Estas estructuras son cruciales en aplicaciones donde se requiere un rendimiento óptimo en la gestión y manipulación de datos, como bases de datos, sistemas de archivos y algoritmos de búsqueda.
- :ledger: [Árbol AVL](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-avl.ipynb)  Introduce los árboles balanceados y las operaciones de rotación para mantener el equilibrio.
  - :page_with_curl: [Aplicaciones de Árboles AVL](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-avl.ipynb)
  - :page_with_curl: [Consideraciones al Implementar un Arbol AVL](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-un-arbol-avl.ipynb)
  - **Implementación de `AVLTree`**
    - :page_with_curl: [Inserción](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/avl-insercion.ipynb)  
    - :page_with_curl: [Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/avl-busqueda.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/avl-eliminacion-de-nodos.ipynb)  
    - :floppy_disk: [AVLTree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/AVLTree.py) 

- :ledger: [Árbol Rojo-Negro](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-rojo-negro.ipynb) : Otro tipo de árbol balanceado, introduce un mecanismo diferente para mantener el balance.
  - :page_with_curl: [Aplicaciones de Árboles Rojo-Negro](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-rojo-negro.ipynb)
  - :page_with_curl: [Consideraciones al Implementar un Arbol Rojo-Negro](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-un-arbol-rojo-negro.ipynb)
  - **Implementación de `RBTree`**
    - :page_with_curl: [Inserción](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/rojo-negro-insercion.ipynb)  
    - :page_with_curl: [Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/rojo-negro-busqueda.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/rojo-negro-eliminacion-de-nodos.ipynb)  
    - :floppy_disk: [RBTree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/RBTree.py) 

- :ledger: [Árbol Splay](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-splay.ipynb) Presenta una estrategia de autoajuste para optimizar las búsquedas secuenciales.
  - :page_with_curl: [Aplicaciones de Árboles Splay](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-splay.ipynb)
  - :page_with_curl: [Consideraciones al Implementar un Arbol Splay](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-un-arbol-splay.ipynb)
  - **Implementación de `SplayTree`**
    - :page_with_curl: [Inserción](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/splay-insercion.ipynb)  
    - :page_with_curl: [Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/splay-busqueda.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/splay-eliminacion-de-nodos.ipynb)  
    - :floppy_disk: [SplayTree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/SplayTree.py) 

---

A continuación los árboles **B**, **B+**, aún siendo estructuras de árbol fundamentales son más complejas y avanzadas, diseñadas para casos de uso específicos, especialmente en sistemas de bases de datos y sistemas de archivos, donde se manejan grandes volúmenes de datos. Estos árboles están optimizados para minimizar el acceso a disco y mejorar la eficiencia en la búsqueda, inserción y eliminación de datos en contextos donde el rendimiento es crítico.

- :ledger: [Arbol B](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-b.ipynb) Balancea inserciones y búsquedas distribuyendo claves en nodos multi-vía.
  - :page_with_curl: [Aplicaciones de Árboles B](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-b.ipynb)
  - :page_with_curl: [Consideraciones al Implementar un Arbol B](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-un-arbol-b.ipynb)
  - **Implementación de `BTree`**
    - :page_with_curl: [Inserción](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/b-insercion.ipynb)  
    - :page_with_curl: [Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/b-busqueda.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/b-eliminacion-de-nodos.ipynb)  
    - :floppy_disk: [BTree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/BPlusTree.py) 

- :ledger: [Arbol B+](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-bplus.ipynb) Extiende Árboles B, manteniendo datos solo en hojas para recorridos secuenciales optimizados.
  - :page_with_curl: [Aplicaciones de Árboles B+](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/aplicaciones-arboles-bplus.ipynb)
  - :page_with_curl: [Consideraciones al Implementar un Arbol B+](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/consideraciones-al-implementar-un-arbol-b+.ipynb)
  - **Implementación de `BPlusTree`**
    - :page_with_curl: [Inserción](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/bplus-insercion.ipynb)  
    - :page_with_curl: [Búsqueda](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/bplus-busqueda.ipynb)  
    - :page_with_curl: [Eliminación de nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/bplus-eliminacion-de-nodos.ipynb)  
    - :floppy_disk: [BTree.py](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/src/BPlusTree.py) 

## Apendices

  - :page_with_curl: [Estructuras de Datos y Nodos](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/estructuras-de-datos-y-nodos.ipynb) (merge)  
  - :page_with_curl: [Comparación Árboles B y B+](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/notebook/arboles/arbol-bb+.ipynb) 