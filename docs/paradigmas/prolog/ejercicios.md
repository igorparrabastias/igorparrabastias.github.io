# Prolog: ejercicios y mini‑demos 🟢

En la **programación lógica** no escribes _cómo_ resolver el problema, sino _qué_ es verdad: declaras **hechos** y **reglas**, y el motor de Prolog se encarga del resto mediante **unificación** y **backtracking**. Tú haces preguntas; él busca todas las formas de hacerlas ciertas.

Esta página reúne una colección de pequeños programas propios con los que fui explorando esas ideas, de lo más elemental (hechos y reglas) a la recursión, las listas y hasta dibujar fractales.

> [!TIP]
> La mejor manera de leer Prolog es al revés: empieza por la **pregunta** que quieres responder (`?- llueve(jueves).`) y deja que el motor descomponga el problema en sub‑preguntas. Tú declaras el mundo; él juega al detective. 🔍

---

## 1. Hechos y reglas: gustos, citas y amistades

El "hola mundo" de la lógica: tres hechos `likes/2` y dos reglas que **derivan** conocimiento nuevo a partir de ellos. `dating/2` exige que el aprecio sea mutuo (conjunción `,`), mientras que `friendship/2` se conforma con que vaya en cualquier dirección (disyunción `;`).

```prolog
--8<-- "learning/programming/prolog/dating.pl"
```

Conceptos que ilustra: **hechos**, **reglas**, **variables**, y la diferencia entre **conjunción** (`,` = "y") y **disyunción** (`;` = "o"). Prueba `?- dating(X, Y).` y observa cómo el backtracking enumera las parejas.

---

## 2. Encadenar reglas: ¿llueve el jueves?

Un clásico de inferencia encadenada. Para saber si `llueve(X)`, Prolog necesita que esté `nublado(X)` **y** `frio(X)`; cada una de esas, a su vez, depende de otros hechos. Es una cadena de razonamiento hacia atrás (_backward chaining_) en estado puro.

```prolog
--8<-- "learning/programming/prolog/lluvia.pl"
```

Con solo dos hechos (`temperatura(jueves, baja)` y `sin_sol(jueves)`), el motor deduce que `llueve(jueves)` es cierto. Ilustra cómo las reglas se **componen** sin que tú dirijas el orden de evaluación.

---

## 3. Backtracking con sabor: la comida de Sam

Una demo didáctica para _ver_ el backtracking en acción. ¿Le gusta a Sam un plato? Depende: le gusta la comida india **suave**, toda la china, toda la italiana… y las patatas fritas pase lo que pase. Cuando una vía falla (un plato indio que no es suave), Prolog **retrocede** y prueba la siguiente regla.

```prolog
--8<-- "learning/programming/prolog/likes.pl"
```

Conceptos: **cláusulas alternativas** para un mismo predicado, **backtracking** y búsqueda en profundidad. Las consultas de ejemplo van anotadas en el propio archivo (`?- likes(sam, dahl).` es cierto; `?- likes(sam, curry).` falla porque el curry no es suave).

---

## 4. Recursión y cierre transitivo: linaje de lenguajes

Aquí entra la **recursión**, el corazón de Prolog. Tenemos hechos `link/2` que conectan un lenguaje con su sucesor (Fortran → Algol60 → CPL → BCPL → C → C++…). La regla `path/2` calcula si existe un **camino** de cualquier longitud entre dos lenguajes: el caso base (`path(L, L)`) y el caso recursivo (da un paso y sigue).

```prolog
--8<-- "learning/programming/prolog/links.pl"
```

Esto es, ni más ni menos, el **cierre transitivo** de un grafo expresado en dos líneas. Pregunta `?- path(fortran, cplusplus).` o, mejor aún, `?- path(fortran, X).` para enumerar todos los descendientes.

---

## 5. Listas y unificación: `append/3`

El predicado más emblemático de Prolog. `append/3` relaciona dos listas con su concatenación, y lo bonito es que es **reversible**: sirve para concatenar, para partir una lista en todos sus trozos posibles, o para comprobar pertenencia. Todo cae por el patrón `[H|T]` (cabeza/cola) y la **unificación**.

```prolog
--8<-- "learning/programming/prolog/append.pl"
```

> [!NOTE]
> Ojo al detalle: en mi copia la segunda cláusula usa `:=` en lugar del `:-` habitual de Prolog. Lo dejo tal cual como recordatorio de lo fácil que es que un solo carácter cambie un "hecho con asignación" por una "regla". En SWI‑Prolog, la versión canónica es `append([H|X], Y, [H|Z]) :- append(X, Y, Z).` 😅

Conceptos: **listas**, patrón **cabeza|cola**, **unificación** y predicados **reversibles**.

---

## 6. Un autómata finito en Prolog

A pesar del nombre del archivo, este ejemplo no son las Torres de Hanói: implementa un **autómata finito** que reconoce un lenguaje. Modela los estados (`inicial/1`, `final/1`) y las transiciones (`delta/3`), y `aceptar/2` recorre recursivamente la lista de símbolos consumiendo uno en cada paso hasta llegar (o no) a un estado final.

```prolog
--8<-- "learning/programming/prolog/hanoi.pl"
```

> [!NOTE]
> La sintaxis (`%domains`, `%predicates`, `readterm/2`, el bloque `%goal`) es de **Turbo/Visual Prolog**, no de SWI‑Prolog, así que no corre tal cual en un intérprete moderno. Lo conservo como ejemplo histórico de cómo se modelan **máquinas de estados** declarativamente: las transiciones son hechos, y el reconocimiento es una recursión sobre la cadena de entrada.

Conceptos: **autómatas finitos**, transiciones como hechos, **recursión sobre listas**.

---

## 7. Fractales con gráficos: el árbol recursivo

Para cerrar con algo visual: un árbol fractal dibujado con la biblioteca gráfica **XPCE** de SWI‑Prolog. La recursión vuelve a ser la protagonista: cada rama dibuja una línea y luego se llama a sí misma dos veces (a ±30°) con una profundidad menor, hasta que `Depth` llega a 0 y el caso base detiene la recursión.

```prolog
--8<-- "learning/programming/prolog/rosseta.pl"
```

Conceptos: **recursión con doble llamada** (árbol de recursión literal), caso base, y trigonometría con `is/2`. Una buena demostración de que Prolog también sabe pintar. 🌳

---

## Ver en GitHub

Todo el código de esta página vive en el repositorio:

- [append.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/append.pl)
- [dating.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/dating.pl)
- [hanoi.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/hanoi.pl)
- [likes.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/likes.pl)
- [links.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/links.pl)
- [lluvia.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/lluvia.pl)
- [rosseta.pl](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/prolog/rosseta.pl)
