# PingPong: procesos que se pasan la pelota 🏓

En el paradigma **funcional y concurrente**, la unidad de trabajo no es el objeto ni el hilo del sistema operativo: es el **proceso de la BEAM** (la máquina virtual de Erlang sobre la que corre Elixir). Son baratísimos —puedes tener millones—, no comparten memoria y solo se comunican **enviándose mensajes**. Este experimento es la forma más pequeña posible de ver esa idea en acción antes de pensar en APIs o microservicios.

> [!TIP]
> Si vienes de la programación con hilos y candados, prepárate para un alivio: aquí no hay memoria compartida que proteger. Cada proceso es una islita con su propio buzón. La "concurrencia" se reduce a escribir cartas. ✉️

## El encaje: de un juego a una arquitectura

El README original deja ver la intención real del experimento: tantear Elixir para construir **APIs y microservicios**.

```
--8<-- "learning/programming/elixir/pingpong/README.md"
```

La pregunta clave que aparece ahí —*"¿Podrán hablar procesos correspondientes a usuarios relacionados?"* y *"Workers para tareas encoladas, en particular actualizar timelines de seguidores"*— es exactamente el patrón de un sistema tipo red social. Y ese patrón empieza, en su forma más reducida, con dos procesos que se mandan `:ping` y `:pong`.

## El corazón: `receive`, el buzón y la recursión

Toda la lección está en este módulo. Un proceso ejecuta `loop/0`, que bloquea en `receive` hasta que llega un mensaje, responde, y **se vuelve a llamar a sí mismo**. Esa recursión es el equivalente funcional de un bucle infinito: no hay variable mutable que incrementar, solo una función que se reinvoca.

```elixir
--8<-- "learning/programming/elixir/pingpong/ping_pong/lib/ping.ex"
```

Tres ideas del paradigma condensadas aquí:

- **Pattern matching en el buzón.** `receive` no usa `if`; declara *formas* de mensaje (`{:pong, from}` y `{:ping, from}`) y la BEAM elige la cláusula que encaja con el primer mensaje de la cola.
- **Inmutabilidad y aislamiento.** `from` es el PID de quien escribió; se responde con `send(from, ...)`. Nadie toca el estado de nadie.
- **Recursión como bucle.** `loop()` al final mantiene vivo al proceso para atender el siguiente mensaje. Sin ella, el proceso moriría tras una sola respuesta (de hecho, así era la primera versión, comentada arriba).

## La prueba: arrancar un proceso y hablarle

El test muestra el ciclo completo de vida: `spawn/3` crea el proceso, `send/2` le manda un mensaje y `assert_receive` espera la respuesta. El operador `^ping` (pin) fija el PID para hacer *match* exacto: "quiero el ping que viene precisamente de ese proceso".

```elixir
--8<-- "learning/programming/elixir/pingpong/ping_pong/test/ping_pong_test.exs"
```

## El esqueleto Mix

Es un proyecto Mix mínimo. Interesa ver que la aplicación solo declara `:logger` y ninguna dependencia: todo lo concurrente viene "de fábrica" en la BEAM, no en una librería.

```elixir
--8<-- "learning/programming/elixir/pingpong/ping_pong/mix.exs"
```

## Para llevarte

Este juguete contiene, en miniatura, el modelo de actores que hace de Elixir/Erlang un lenguaje natural para sistemas distribuidos y tolerantes a fallos: procesos aislados + mensajes + supervisión. Un timeline de seguidores no es más que muchos de estos `loop` corriendo a la vez. 🚀

> [Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/elixir/pingpong)
