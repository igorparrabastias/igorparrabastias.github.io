# El Event Loop de Node.js

¿Cómo puede Node.js ser *single-thread* y, aun así, atender miles de conexiones a la vez sin bloquearse? La respuesta es el **event loop**: el corazón que late dentro del runtime y decide qué callback se ejecuta y cuándo. En esta página abrimos el capó y miramos cómo funciona Node por dentro.

Todo el código embebido es **código real** del laboratorio, leído directamente desde `learning/programming/node.js/event-loop/`. Si tocas el archivo fuente, esta página se actualiza sola.

> [!TIP]
> El event loop es como un camarero hiperactivo en un restaurante de un solo mozo: toma tu pedido, lo manda a cocina y, en vez de quedarse mirando la sartén, atiende a la siguiente mesa. Cuando el plato está listo, vuelve a tu mesa. Nunca se bloquea, solo reparte su atención. 🍽️

---

## Las fases del event loop

El event loop no es una cola única: es un ciclo con **fases** bien definidas, y en cada vuelta (un *tick*) las recorre en orden. Cada fase tiene su propia cola de callbacks. Este diagrama, sacado de los apuntes, lo resume mejor que mil palabras:

```bash
--8<-- "learning/programming/node.js/event-loop/event-loop-phases.bash"
```

Las fases que más nos interesan:

- **timers**: ejecuta los callbacks de `setTimeout` y `setInterval` cuyo tiempo ya venció.
- **pending callbacks**: callbacks de ciertas operaciones del sistema (por ejemplo, algunos errores de TCP).
- **poll**: el corazón del asunto. Aquí Node recupera nuevos eventos de I/O (lectura de ficheros, conexiones de red) y ejecuta sus callbacks. Si no hay nada pendiente, **espera** aquí.
- **check**: ejecuta los callbacks de `setImmediate`.
- **close callbacks**: callbacks de cierre, como `socket.on('close', ...)`.

Aparte del ciclo viven dos colas con **prioridad especial** que se vacían *entre* fases: `process.nextTick()` (la más prioritaria) y las *microtasks* de las promesas.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/event-loop-phases.bash)

---

## Lo más simple: dos timers

Antes de complicarnos, fijemos la idea base. El código síncrono se ejecuta **primero, de arriba abajo**; los `setTimeout` quedan agendados para más tarde, aunque su retraso sea de `0`:

```javascript
--8<-- "learning/programming/node.js/event-loop/timeout.js"
```

Aquí el orden es claro: primero se imprime `2` (síncrono), luego `1` (al segundo) y por último `3` (a los dos segundos). El `console.log(2)` "se cuela" porque los timers nunca disparan antes de que termine el código síncrono del *tick* actual.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/timeout.js)

---

## El ejemplo que lo demuestra todo

Este es el ejemplo estrella: mezcla `setTimeout`, `setImmediate`, `process.nextTick` y un callback de `fs.readFile`. Predecir su salida es un ejercicio clásico (y traicionero) para entender de verdad las fases.

```javascript
--8<-- "learning/programming/node.js/event-loop/event-loop.js"
```

Cosas a observar:

- `process.nextTick(next)` se llama a sí mismo recursivamente. La cola de `nextTick` se vacía **por completo** antes de pasar a la siguiente fase... así que esto **mata de hambre** (*starvation*) al resto del event loop: `next` se imprime sin parar y los demás callbacks nunca llegan. Es la trampa clásica de abusar de `nextTick`.
- Dentro del callback de `fs.readFile` (que corre en la fase **poll**), un `setImmediate` (fase **check**) se ejecuta *antes* que un `setTimeout`, porque check viene justo después de poll en la misma vuelta.

> [!TIP]
> Si quieres ver la versión "sana" que NO bloquea el loop, mira [`event-loop-fix-next.js`](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/event-loop-fix-next.js): basta con que `next` **no** se reagende a sí mismo.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/event-loop.js)

---

## Por qué importa: un servidor HTTP

Toda esta maquinaria existe para esto: un servidor que atiende peticiones sin lanzar un hilo por cada cliente. Cuando llega una petición, su callback entra por la fase **poll**; mientras no llega nada, el loop simplemente espera ahí sin quemar CPU.

```javascript
--8<-- "learning/programming/node.js/event-loop/http-server.js"
```

`server.listen()` no bloquea: registra el servidor y devuelve el control. El event loop se queda "vivo" esperando conexiones, y por eso el proceso no termina solo.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/http-server.js)

---

## El motor por dentro: libuv

El event loop no está escrito en JavaScript, sino en **C**, dentro de la librería [libuv](https://libuv.org/). Si miramos el corazón de la función `uv_run`, vemos las fases con nuestros propios ojos: el `while` es el "loop", y cada `uv__run_*` es una fase:

```c
--8<-- "learning/programming/node.js/event-loop/node-event-loop-core.c"
```

Reconócelas: `uv__run_timers` (timers), `uv__run_pending` (pending callbacks), `uv__io_poll` (poll), `uv__run_check` (check, donde viven los `setImmediate`) y `uv__run_closing_handles` (close callbacks). Ese diagrama de cajitas de arriba es, literalmente, este `while`.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/node-event-loop-core.c)

---

## Más ejemplos en el laboratorio

En la carpeta hay más piezas para experimentar:

- [`simple-timer-immediate.js`](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/simple-timer-immediate.js) — juega con `setTimeout`, `setImmediate`, `setInterval` y `clearImmediate`.
- [`file-read.js`](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/event-loop/file-read.js) — el caso mínimo de I/O asíncrono con `fs.readFile`.

> Fuente de inspiración de estos apuntes: [*A Short Introduction to Node.js Event Loop*](https://medium.com/swlh/a-short-introduction-to-node-js-event-loop-558f6f2c2af7).
