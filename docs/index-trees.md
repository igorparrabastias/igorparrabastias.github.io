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

- :ledger: [Arboles](notebook/arboles/introduccion.html) Introducción general a árboles. Terminología y consideraciones de implementación.
  - :page_with_curl: [Tipos de Árboles](notebook/arboles/tipos-de-arboles.html) Tipos principales y su categorización según su estructura y propósito.
  - :page_with_curl: [Algoritmos Relacionados con Árboles](notebook/arboles/algoritmos-relacionados-con-arboles.html)
  - :page_with_curl: [Ejemplo de Algoritmo en Sistemas de Recomendación](notebook/arboles/ejemplo-de-algoritmo-en-sistemas-de-recomendacion.html)
  - :page_with_curl: [Ejemplo de Algoritmo par Procesamiento del Lenguaje Natural](notebook/arboles/ejemplo-de-algoritmo-par-procesamiento-del-lenguaje-natural.html)
  - :page_with_curl: [Ejemplo de Algoritmo en Bioinformática](notebook/arboles/ejemplo-de-algoritmo-en-bioinformatica.html)
  - **Implementación de `Tree`**
    - :page_with_curl: [Implementación Básica de Arbol](notebook/arboles/tree-elemental.html)  
    - :floppy_disk: [Tree.py](notebook/arboles/src/Tree.py)
  <!-- - :page_with_curl: [Ejercicios](notebook/arboles/ejercicios.html)   -->

- :ledger: [Árboles Binarios](notebook/arboles/arbol-binario.html) Concepto básico y recorridos.
  - :page_with_curl: [Aplicaciones de Árboles Binarios](notebook/arboles/aplicaciones-arboles-binarios.html)
  - :page_with_curl: [Consideraciones al Implementar un Arbol Binario](notebook/arboles/consideraciones-al-implementar-un-arbol-binario.html)
  - **Implementación de `BinaryTree`**
    - :page_with_curl: [Inserción manual](notebook/arboles/insercion-manual.html)  
    - :page_with_curl: [Inserción automática](notebook/arboles/insercion-automatica.html)  
    - :page_with_curl: [Búsqueda recursiva](notebook/arboles/busqueda-recursiva.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/eliminacion-de-nodos.html) 
    - :floppy_disk: [BinaryTree.py](notebook/arboles/src/BinaryTree.py) 
  - **Métodos de Recorrido**
    - :page_with_curl: [preorder (DFS)](notebook/arboles/implementacion-preorder.html)
    - :page_with_curl: [inorder (DFS)](notebook/arboles/implementacion-inorder.html)
    - :page_with_curl: [postorder (DFS)](notebook/arboles/implementacion-postorder.html)
    - :page_with_curl: [level_order (BFS)](notebook/arboles/implementacion-level_order.html)
  - **Métodos de Utilidad**
    - :page_with_curl: [height](notebook/arboles/implementacion-height.html)
    - :page_with_curl: [size](notebook/arboles/implementacion-size.html)
    - :page_with_curl: [is_balanced](notebook/arboles/implementacion-is_balanced.html)
  - **Métodos Avanzados**
    - :page_with_curl: [mirror](notebook/arboles/implementacion-mirror.html)
    - :page_with_curl: [is_tree](notebook/arboles/implementacion-is_tree.html)
    - :page_with_curl: [convert_to_linked_list](notebook/arboles/implementacion-convert_to_linked_list.html)
    - :page_with_curl: [serialize_deserialize](notebook/arboles/implementacion-serialize_deserialize.html)

- :ledger: [Árboles Binarios de Búsqueda (BST)](notebook/arboles/arbol-binario-de-busqueda-bst.html)  Evolución del árbol binario, introduce la idea de ordenamiento y eficiencia en la búsqueda.
  - :page_with_curl: [Aplicaciones de Árboles Binarios de Búsqueda](notebook/arboles/aplicaciones-arboles-binarios-de-busqueda.html)
  - :page_with_curl: [Consideraciones al Implementar Métodos para BST](notebook/arboles/consideraciones-al-implementar-metodos-para-bst.html)
  - **Implementación de `BST`**
    - :page_with_curl: [Inserción](notebook/arboles/bst-insercion.html)  
    - :page_with_curl: [Búsqueda](notebook/arboles/bst-busqueda.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/bst-eliminacion-de-nodos.html)  
    - :floppy_disk: [BST.py](notebook/arboles/src/BST.py) 
  - **Métodos de Utilidad**
    - :page_with_curl: [get_successor](notebook/arboles/implementacion-get_successor.html)
    - :page_with_curl: [get_predecessor](notebook/arboles/implementacion-get_predecessor.html)
    - :page_with_curl: [lowest_common_ancestor](notebook/arboles/implementacion-lowest_common_ancestor.html)
  - **Métodos Avanzados**
    - :page_with_curl: [is_bst](notebook/arboles/implementacion-is_bst.html)
    - :page_with_curl: [is_subtree](notebook/arboles/implementacion-is_subtree.html)
    - :page_with_curl: [find_level](notebook/arboles/implementacion-find_level.html)
    - :page_with_curl: [bst_convert_to_linked_list](notebook/arboles/implementacion-bst_convert_to_linked_list.html)
    - :page_with_curl: [bst_serialize_deserialize](notebook/arboles/implementacion-bst_serialize_deserialize.html)

Los árboles **AVL**, **rojo-negro** y **splay** son variantes avanzadas de los **árboles binarios de búsqueda**, diseñadas para mejorar el rendimiento en operaciones de inserción, eliminación y búsqueda. Los **árboles AVL** mantienen un equilibrio óptimo, asegurando que la diferencia de altura entre subárboles no supere un valor específico, lo que garantiza tiempos de búsqueda consistentes. Los **árboles rojo-negro**, por otro lado, aplican reglas de coloración para mantener un equilibrio relajado, lo que los hace más eficientes en operaciones de inserción y eliminación. Mientras tanto, los **árboles splay** utilizan rotaciones y reorganizaciones dinámicas para llevar a los nodos más accesibles a la raíz, optimizando las operaciones de búsqueda. Estas estructuras son cruciales en aplicaciones donde se requiere un rendimiento óptimo en la gestión y manipulación de datos, como bases de datos, sistemas de archivos y algoritmos de búsqueda.
- :ledger: [Árbol AVL](notebook/arboles/arbol-avl.html)  Introduce los árboles balanceados y las operaciones de rotación para mantener el equilibrio.
  - :page_with_curl: [Aplicaciones de Árboles AVL](notebook/arboles/aplicaciones-arboles-avl.html)
  - :page_with_curl: [Consideraciones al Implementar un Arbol AVL](notebook/arboles/consideraciones-al-implementar-un-arbol-avl.html)
  - **Implementación de `AVLTree`**
    - :page_with_curl: [Inserción](notebook/arboles/avl-insercion.html)  
    - :page_with_curl: [Búsqueda](notebook/arboles/avl-busqueda.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/avl-eliminacion-de-nodos.html)  
    - :floppy_disk: [AVLTree.py](notebook/arboles/src/AVLTree.py) 

- :ledger: [Árbol Rojo-Negro](notebook/arboles/arbol-rojo-negro.html) : Otro tipo de árbol balanceado, introduce un mecanismo diferente para mantener el balance.
  - :page_with_curl: [Aplicaciones de Árboles Rojo-Negro](notebook/arboles/aplicaciones-arboles-rojo-negro.html)
  - :page_with_curl: [Consideraciones al Implementar un Arbol Rojo-Negro](notebook/arboles/consideraciones-al-implementar-un-arbol-rojo-negro.html)
  - **Implementación de `RBTree`**
    - :page_with_curl: [Inserción](notebook/arboles/rojo-negro-insercion.html)  
    - :page_with_curl: [Búsqueda](notebook/arboles/rojo-negro-busqueda.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/rojo-negro-eliminacion-de-nodos.html)  
    - :floppy_disk: [RBTree.py](notebook/arboles/src/RBTree.py) 

- :ledger: [Árbol Splay](notebook/arboles/arbol-splay.html) Presenta una estrategia de autoajuste para optimizar las búsquedas secuenciales.
  - :page_with_curl: [Aplicaciones de Árboles Splay](notebook/arboles/aplicaciones-arboles-splay.html)
  - :page_with_curl: [Consideraciones al Implementar un Arbol Splay](notebook/arboles/consideraciones-al-implementar-un-arbol-splay.html)
  - **Implementación de `SplayTree`**
    - :page_with_curl: [Inserción](notebook/arboles/splay-insercion.html)  
    - :page_with_curl: [Búsqueda](notebook/arboles/splay-busqueda.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/splay-eliminacion-de-nodos.html)  
    - :floppy_disk: [SplayTree.py](notebook/arboles/src/SplayTree.py) 

---

A continuación los árboles **B**, **B+**, aún siendo estructuras de árbol fundamentales son más complejas y avanzadas, diseñadas para casos de uso específicos, especialmente en sistemas de bases de datos y sistemas de archivos, donde se manejan grandes volúmenes de datos. Estos árboles están optimizados para minimizar el acceso a disco y mejorar la eficiencia en la búsqueda, inserción y eliminación de datos en contextos donde el rendimiento es crítico.

- :ledger: [Arbol B](notebook/arboles/arbol-b.html) Balancea inserciones y búsquedas distribuyendo claves en nodos multi-vía.
  - :page_with_curl: [Aplicaciones de Árboles B](notebook/arboles/aplicaciones-arboles-b.html)
  - :page_with_curl: [Consideraciones al Implementar un Arbol B](notebook/arboles/consideraciones-al-implementar-un-arbol-b.html)
  - **Implementación de `BTree`**
    - :page_with_curl: [Inserción](notebook/arboles/b-insercion.html)  
    - :page_with_curl: [Búsqueda](notebook/arboles/b-busqueda.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/b-eliminacion-de-nodos.html)  
    - :floppy_disk: [BTree.py](notebook/arboles/src/BTree.py) 

- :ledger: [Arbol B+](notebook/arboles/arbol-bplus.html) Extiende Árboles B, manteniendo datos solo en hojas para recorridos secuenciales optimizados.
  - :page_with_curl: [Aplicaciones de Árboles B+](notebook/arboles/aplicaciones-arboles-bplus.html)
  - :page_with_curl: [Consideraciones al Implementar un Arbol B+](notebook/arboles/consideraciones-al-implementar-un-arbol-b+.html)
  - **Implementación de `BPlusTree`**
    - :page_with_curl: [Inserción](notebook/arboles/bplus-insercion.html)  
    - :page_with_curl: [Búsqueda](notebook/arboles/bplus-busqueda.html)  
    - :page_with_curl: [Eliminación de nodos](notebook/arboles/bplus-eliminacion-de-nodos.html)  
    - :floppy_disk: [BTree.py](notebook/arboles/src/BTree.py) 

## Apendices

  - :page_with_curl: [Estructuras de Datos y Nodos](notebook/arboles/estructuras-de-datos-y-nodos.html) (merge)  
  - :page_with_curl: [Comparación Árboles B y B+](notebook/arboles/arbol-bb+.html) 