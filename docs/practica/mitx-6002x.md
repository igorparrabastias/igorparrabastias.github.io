# MITx 6.00.2x — Computational Thinking and Data Science

La continuación natural de [6.00.1x](mitx-6001x.md): **[Introduction to Computational Thinking and Data Science](https://www.edx.org/learn/data-science/massachusetts-institute-of-technology-introduction-to-computational-thinking-and-data-science)** (MITx 6.00.2x). Aquí el foco se mueve de "saber programar" a **usar la programación para resolver problemas**: optimización, algoritmos voraces (*greedy*) frente a fuerza bruta, modelos estocásticos, simulaciones de Montecarlo y una introducción al análisis de datos.

> [!NOTE]
> 🟡 Curso mixto. Enunciados, datos y *helpers* son del MIT; mi trabajo es el código de los *problem sets*. Solo embebo mis archivos.
>
> Crédito y curso original: **[MITx 6.00.2x en edX](https://www.edx.org/learn/data-science/massachusetts-institute-of-technology-introduction-to-computational-thinking-and-data-science)**. Mi copia del material: [learning/courses/MITx 6.00.2x](https://github.com/igorparrabastias/igorparrabastias.github.io/tree/main/learning/courses/MITx%206.00.2x).

## Problem Set 1 — Space Cows 🐄🚀

El enunciado es delicioso: una colonia de aliens bioingenieros (los *Aucks*) ha creado vacas mutantes que saltan sobre la Luna y quiere llevárselas a su planeta. La nave tiene un **límite de peso** y los aliens quieren minimizar el número de viajes. Es, en el fondo, una variante del problema de *bin packing*:

- **Parte A — `greedy_cow_transport`**: heurística voraz. En cada viaje mete la vaca más pesada que quepa hasta llenar la nave. Rápido, pero no necesariamente óptimo.
- **Parte B — `brute_force_cow_transport`**: enumera **todas** las particiones posibles de las vacas y se queda con la que use menos viajes respetando el límite. Óptimo, pero explota en cuanto crece el número de vacas.
- **Parte C — `compare_cow_transport_algorithms`**: ejecuta ambas y compara número de viajes y tiempo de cómputo. La moraleja clásica: voraz ≠ óptimo, y óptimo ≠ asequible.

El *scaffolding* del problema (con los enunciados y la carga de datos desde `ps1_cow_data.txt`) es este:

```python
--8<-- "learning/courses/MITx 6.00.2x/ps1/ps1.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/courses/MITx%206.00.2x/ps1/ps1.py)

> [!NOTE]
> Honestidad ante todo: este `ps1.py` conserva los `TODO`/`pass` de las tres funciones. Está aquí como **punto de partida del problema**, no como solución terminada. Es una de mis asignaturas pendientes del repo. 😇

### Helper de particiones

Para la fuerza bruta hace falta generar todas las particiones de un conjunto. El curso aporta este *helper* (`get_partitions`), basado en un hilo de *Code Review* de Stack Overflow, que entrega cada partición lista para iterar:

```python
--8<-- "learning/courses/MITx 6.00.2x/ps1/ps1_partition.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/courses/MITx%206.00.2x/ps1/ps1_partition.py)

> [!TIP]
> ¿Por qué la fuerza bruta se vuelve impracticable? Porque el número de particiones de un conjunto crece como los **números de Bell**, más rápido que la exponencial. Por eso existen las heurísticas: a veces "bastante bueno y ya" gana a "perfecto pero el lunes que viene".
