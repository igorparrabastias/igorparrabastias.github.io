# Ejercicios sueltos: pattern matching y recursión a la vista

Tres mini-programas de calentamiento (estilo Exercism) que caben en una pantalla pero condensan los gestos esenciales del paradigma funcional en Elixir: **pattern matching**, **guardas**, **rangos** y la **tubería `|>`**. Nada de bucles `for`, nada de variables que mutan. Datos que entran, datos que salen.

> [!TIP]
> En Elixir resolver un problema suele ser "describir las formas que puede tener un dato y qué hacer con cada una", no "decirle a la máquina paso a paso qué tocar". Si te pillas escribiendo un `if` gigante, casi siempre hay un *match* más bonito esperando. ✨

## `hw.ex` — el saludo de rigor

El más simple de todos: un módulo, una función, un efecto.

```elixir
--8<-- "learning/programming/elixir/exercism/hw.ex"
```

Poco que comentar, salvo la convención: la lógica vive en un `defmodule`, y `IO.puts/1` es el efecto de salida. Es el "encender la máquina".

## `gm.ex` — eligiendo con `cond`

Aquí ya hay decisión. `cond` evalúa condiciones en orden y devuelve la primera que sea verdadera (con `true ->` como caso por defecto). Y mira la tubería: `option |> g |> IO.puts()` lee de izquierda a derecha como una receta: *toma la opción, conviértela en saludo, imprímela*.

```elixir
--8<-- "learning/programming/elixir/exercism/gm.ex"
```

Detalle de estilo: `g/1` es **privada** (`defp`) porque es un ayudante interno; solo `print/1` es la interfaz pública del módulo.

## `fizzbuzz.ex` — la joya: pattern matching con guardas

Este es el ejemplo estrella. El clásico FizzBuzz, que en lenguajes imperativos se resuelve con un `if/else if` anidado, aquí se descompone en **cuatro cláusulas de la misma función** `check/1`, cada una con una **guarda** (`when`):

```elixir
--8<-- "learning/programming/elixir/exercism/fizzbuzz.ex"
```

Lo que hay que mirar con lupa:

- **El orden importa.** Elixir prueba las cláusulas de arriba abajo y ejecuta la primera que encaja. Por eso `rem(number, 15) == 0` (FizzBuzz) va **primero**: un múltiplo de 15 también lo es de 3 y de 5, así que debe atraparse antes.
- **Guardas en vez de `if`.** Cada caso es una función completa con su condición de entrada. La lógica de decisión desaparece del *cuerpo* y sube a la *firma*. Es declarativo: cada línea dice "para este tipo de número, esto".
- **Rangos + `Enum.each`.** `first..last |> Enum.each(...)` recorre el rango sin un índice mutable a la vista. Iterar es aplicar una función a cada elemento, no avanzar un contador.
- **La cláusula final** `check(number)` sin guarda es el "para todo lo demás": el caso base que imprime el número tal cual.

## Para llevarte

Estos tres ejercicios muestran la progresión natural del paradigma: del efecto puro (`hw`), a la decisión expresada como datos (`gm`), hasta la **descomposición por casos con pattern matching** (`fizzbuzz`), que es la herramienta que de verdad te cambia la forma de pensar en Elixir. 🧩

> [Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/elixir/exercism)
