# Exercism: katas en Elixir y Python

[Exercism](https://exercism.org) es una plataforma gratuita de ejercicios de programación con *mentoring*. Te dan el esqueleto y una batería de tests; tú escribes la solución hasta que todo pasa en verde. Aquí recojo **mis soluciones** a varios ejercicios, sobre todo del *track* de **Elixir** (un buen patio de recreo para pensar en clave funcional) y el clásico "Hola Mundo" de Python.

> [!NOTE]
> 🟡 Curso mixto. El *scaffolding* y los tests son de Exercism; **el código de solución es mío**. Solo embebo mis archivos de solución (no los `*_test`).
>
> Crédito y ejercicios originales: **[exercism.org](https://exercism.org)**. Mi copia del *track*: [learning/programming/exercism](https://github.com/igorparrabastias/igorparrabastias.github.io/tree/main/learning/programming/exercism).

## Elixir

### Hello World

El ritual de iniciación de cualquier *track*: devolver una cadena. Sirve para validar que el entorno (tests incluidos) está bien montado antes de entrar en harina.

```elixir
--8<-- "learning/programming/exercism/elixir/hello-world/hello_world.exs"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/exercism/elixir/hello-world/hello_world.exs)

### Nucleotide Count

Dada una cadena de ADN (`A`, `C`, `G`, `T`), contar cuántas veces aparece cada nucleótido y devolver un histograma. Es un ejercicio perfecto para enamorarse de `Enum.reduce/3`: la solución acumula sobre la lista sin mutar nada y construye el mapa de frecuencias de forma declarativa.

```elixir
--8<-- "learning/programming/exercism/elixir/nucleotide-count/nucleotide_count.exs"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/exercism/elixir/nucleotide-count/nucleotide_count.exs)

### Secret Handshake

A partir de un número, su representación **binaria** codifica una secuencia de acciones (`wink`, `double blink`, `close your eyes`, `jump`), y el bit `10000` invierte el orden. Aquí entran en juego `Integer.digits(code, 2)`, `Enum.with_index/1` y otra vez `Enum.reduce/3` para ir montando la lista de comandos bit a bit.

```elixir
--8<-- "learning/programming/exercism/elixir/secret-handshake/secret_handshake.exs"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/exercism/elixir/secret-handshake/secret_handshake.exs)

### Bob

Bob es un adolescente lacónico que responde distinto según le grites, le preguntes o le grites una pregunta. Lo dejé **planteado** (el esqueleto de Exercism todavía con su `raise`), así que lo incluyo como tarea pendiente y recordatorio honesto de que no todo en el repo está terminado. 😅

```elixir
--8<-- "learning/programming/exercism/elixir/bob/bob.exs"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/exercism/elixir/bob/bob.exs)

> [!TIP]
> Si quieres atacar Bob tú mismo: la clave es normalizar el input (¿está vacío?, ¿termina en `?`, ¿está todo en mayúsculas?) y decidir la respuesta con un `cond`. Pista funcional: `String.trim`, `String.upcase` y comparar contra el original.

## Python

### Hello World

El mismo rito, en Python. Una línea, pero confirma que el *runner* de tests funciona.

```python
--8<-- "learning/programming/exercism/python/hello-world/hello_world.py"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/exercism/python/hello-world/hello_world.py)
