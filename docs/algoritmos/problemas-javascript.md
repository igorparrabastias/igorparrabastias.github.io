# Problemas resueltos en JavaScript

Aquí ponemos a trabajar las [estructuras](../estructuras/javascript.md) y los [algoritmos](javascript.md) con retos tipo entrevista (varios salidos de LeetCode y GeeksforGeeks), agrupados por tema. Es la versión **JavaScript** de los ejercicios del curso: *el mismo concepto, otra implementación*.

Cada solución es **código real** del laboratorio (`learning/computer-science-basics/problems/`) y cada una viene con sus propios tests en un archivo `.test.js` hermano. Al final muestro un par de esos tests como ejemplo de cómo se verifican.

> [!TIP]
> No leas solo la solución: tapa el código, lee el enunciado e intenta resolverlo tú. El "ajá" de descubrirlo vale más que diez soluciones leídas. 💡

---

## Arrays

### Two Sum
*Dado un array de enteros y un objetivo, devuelve los índices de los dos números que suman ese objetivo.* Solución en una pasada con un `Map` (hash): O(n) tiempo, O(n) espacio.

```javascript
--8<-- "learning/computer-science-basics/problems/twoSumsFromArray.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/twoSumsFromArray.js)

### 3Sum (triplete que suma cero)
*Encuentra todos los tripletes únicos `a, b, c` del array tales que `a + b + c = 0`.* Se ordena el array y, fijando un elemento, se buscan los otros dos con dos punteros: O(n²) (el archivo conserva, comentada, la versión naíf O(n³) para comparar).

```javascript
--8<-- "learning/computer-science-basics/problems/treeSumGivesZero.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/treeSumGivesZero.js)

### Máxima suma de i·arr[i] entre rotaciones
*Dado un array, encuentra el valor máximo de Σ i·arr[i] entre todas sus rotaciones.* El truco es calcular cada rotación a partir de la anterior en O(1), logrando O(n) total y O(1) de espacio.

```javascript
--8<-- "learning/computer-science-basics/problems/maxSumRotationArray.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/maxSumRotationArray.js)

### Par más cercano de dos arrays ordenados
*Dados dos arrays ordenados y un número x, encuentra el par (uno de cada array) cuya suma sea la más cercana a x.* Técnica de **dos punteros** (uno al inicio del primero, otro al final del segundo): O(n) tiempo, O(1) espacio.

```javascript
--8<-- "learning/computer-science-basics/problems/closestPair.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/closestPair.js)

---

## Árboles

### Máxima suma de camino en un árbol binario
*Encuentra la máxima suma de un camino que puede empezar y terminar en cualquier nodo.* Recorrido recursivo que en cada nodo combina lo mejor de sus subárboles izquierdo y derecho: O(n).

```javascript
--8<-- "learning/computer-science-basics/problems/findMaxPathSumBinaryTree.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/findMaxPathSumBinaryTree.js)

### Reconstruir árbol desde inorder + preorder
*Dados los recorridos inorder y preorder, reconstruye el árbol y devuelve su recorrido postorder.* Usa un `Map` para localizar la raíz dentro del inorder en O(1) y construir recursivamente cada subárbol.

```javascript
--8<-- "learning/computer-science-basics/problems/buildTree1.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/buildTree1.js)

---

## Grafos

### DFS de un grafo
*Recorrido en profundidad (DFS) de un grafo conexo no dirigido, empezando por el vértice 0.* Enfoque recursivo con un array de visitados. Tiempo O(V + E), espacio O(V).

```javascript
--8<-- "learning/computer-science-basics/problems/dfsOfGraph.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/dfsOfGraph.js)

---

## Strings y backtracking

### Substring palindrómica más larga
*Encuentra la subcadena palindrómica más larga.* Técnica de **expandir desde el centro**: O(n²) tiempo, O(1) espacio. Hay dos versiones para comparar estilos: `longPalindrome` (todo en un bucle) y `longPalindrome2` (más limpia, con un helper `checkPalindrome` que cubre palíndromos de longitud par e impar).

```javascript
--8<-- "learning/computer-science-basics/problems/longPalindrome.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/longPalindrome.js)

```javascript
--8<-- "learning/computer-science-basics/problems/longPalindrome2.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/longPalindrome2.js)

### Combination Sum
*Dado un array de enteros positivos y una suma objetivo, encuentra todas las combinaciones (con repetición permitida) que suman ese objetivo.* Es el ejemplo de **backtracking** del curso: se añade un número (`temp.push`), se recursa, y si ese camino no funciona se **deshace** la última decisión (`temp.splice`). Esa "vuelta atrás" es exactamente lo que describimos en la [sección de backtracking](javascript.md#backtracking).

```javascript
--8<-- "learning/computer-science-basics/problems/combinationSum.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/combinationSum.js)

---

## ¿Cómo se prueban? (tests con Jest)

Cada solución tiene un archivo `.test.js` que verifica varios casos con **Jest** (`describe` / `it` / `expect`). La idea: importas la `Solution`, la ejecutas con una entrada conocida y compruebas que la salida es la esperada. Dos ejemplos:

**Tests de Two Sum** — varios casos, incluido el array con duplicados `[3, 3]`:

```javascript
--8<-- "learning/computer-science-basics/problems/twoSumsFromArray.test.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/twoSumsFromArray.test.js)

**Tests de DFS** — comprueban el orden exacto del recorrido sobre dos grafos:

```javascript
--8<-- "learning/computer-science-basics/problems/dfsOfGraph.test.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/computer-science-basics/problems/dfsOfGraph.test.js)

> [!TIP]
> Escribir el test *antes* de la solución (TDD) te obliga a entender bien el enunciado: ¿cuál es exactamente la entrada y cuál la salida correcta? Mitad del problema resuelto. ✅
