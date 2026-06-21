# MITx 6.00.1x — Introduction to CS and Programming Using Python

El curso fundacional del MIT en edX: **[Introduction to Computer Science and Programming Using Python](https://www.edx.org/learn/computer-science/massachusetts-institute-of-technology-introduction-to-computer-science-and-programming-using-python)** (MITx 6.00.1x). Cubre lo esencial para empezar a pensar como informático: variables y bucles, cadenas y algoritmos, funciones y recursión, tuplas/listas/diccionarios, depuración y excepciones, clases y herencia, y una primera dosis de **complejidad algorítmica** y algoritmos de búsqueda/ordenación y grafos.

> [!NOTE]
> 🟡 Curso mixto. Los enunciados, *helpers* y materiales son del MIT; **las soluciones a los *problem sets* y exámenes son mías**. Solo embebo mi código.
>
> Crédito y curso original: **[MITx 6.00.1x en edX](https://www.edx.org/learn/computer-science/massachusetts-institute-of-technology-introduction-to-computer-science-and-programming-using-python)**. Mi copia del material: [learning/courses/MITx 6.00.1x](https://github.com/igorparrabastias/igorparrabastias.github.io/tree/main/learning/courses/MITx%206.00.1x).

En el repo están además las **13 lecturas en PDF** (`lec1.pdf` … `lec13_graphs_visualize_new.pdf`), el *syllabus* y las transcripciones de las clases (carpeta `textos/`), todo como material de referencia.

## Problem Set 1 — Cadenas y bucles

### ps1-1: contar vocales

Recorrer la cadena `s` y contar cuántas de sus letras son vocales. Un calentamiento para coger soltura con `for` y pertenencia (`in`).

```python
--8<-- "learning/courses/MITx 6.00.1x/ps1-1.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/courses/MITx%206.00.1x/ps1-1.py)

### ps1-2: cuántas veces aparece "bob"

Contar las apariciones (incluso solapadas) de la subcadena `"bob"`. Mi versión va consumiendo la lista con una ventana de tres caracteres.

```python
--8<-- "learning/courses/MITx 6.00.1x/ps1-2.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/courses/MITx%206.00.1x/ps1-2.py)

## Problem Set 4 — El juego de palabras (Word Game)

Un mini-Scrabble por terminal: repartir una mano de letras, puntuar palabras según los valores de Scrabble (con bonus de +50 si usas todas las letras) y validar contra un diccionario (`words.txt`). Aquí ya se nota el salto: diccionarios de frecuencias, gestión de estado de la mano y varias funciones colaborando.

```python
--8<-- "learning/courses/MITx 6.00.1x/ps4/ps4a.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/courses/MITx%206.00.1x/ps4/ps4a.py)

## Problem Set 6 — Cifrado César

Descifrar un chiste oculto con un cifrado por desplazamiento (César). La gracia está en **probar todos los desplazamientos** y quedarse con el que produzca más palabras válidas del diccionario: un primer contacto con la idea de "fuerza bruta guiada por una métrica".

```python
--8<-- "learning/courses/MITx 6.00.1x/ps6/ps6.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/courses/MITx%206.00.1x/ps6/ps6.py)

> [!TIP]
> Si vienes de [los Fundamentos de Python](../python/index.md), este curso es el banco de pruebas ideal: lo que allí lees como teoría, aquí toca sudarlo en *problem sets* con tests.
