# Fundamentos de Node.js

Antes de montar servidores y APIs conviene conocer las piezas básicas que trae Node de fábrica: cómo maneja datos binarios, cómo emite y escucha eventos, cómo habla con la terminal y cómo escribe logs. Esta página recorre esos fundamentos con ejemplos pequeños y autocontenidos.

> Casi todo Node está construido alrededor de una **arquitectura asíncrona y orientada a eventos**. Las APIs del núcleo, como `fs` o `net`, usan eventos para comunicarse con tu programa.

Todo el código embebido es **código real** del laboratorio, leído desde `learning/programming/node.js/fundamentals/`. Si tocas el archivo fuente, esta página se actualiza sola.

> [!TIP]
> Estos ejemplos están pensados para ejecutarse con `node archivo.js` y mirar la salida. No hay mejor forma de aprender Node que romper estos scripts y ver qué pasa. 🔧

---

## Buffers: datos binarios en crudo

La clase `Buffer` representa secuencias de bytes (enteros de 0 a 255). Está basada en `Uint8Array` y sirve para manipular datos binarios: ficheros, streams de red, etc. Es una API de bajo nivel, así que rara vez la usarás directamente, pero entenderla ayuda mucho.

```javascript
--8<-- "learning/programming/node.js/fundamentals/buffer.js"
```

Detalles curiosos del ejemplo: `Buffer.alloc(10)` reserva 10 bytes a cero; `allocUnsafe` es más rápido pero puede traer "basura" de memoria; y `Buffer.from([265, 6.5, -255, '7'])` muestra cómo se truncan/normalizan los valores que no caben en un byte.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/fundamentals/buffer.js)

---

## EventEmitter: el patrón observador

`EventEmitter` es la columna vertebral del modelo de eventos de Node. Un objeto **emite** eventos (`emit`) y otros se **suscriben** (`on`, `once`). Es el mismo patrón que usan los servidores, los streams y casi todo el ecosistema.

```javascript
--8<-- "learning/programming/node.js/fundamentals/events.js"
```

Fíjate en `once`: el listener se dispara **una sola vez** aunque emitas el evento tres veces. Y el evento `'error'` es especial: si lo emites sin tener un listener registrado, Node lanza una excepción no capturada.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/fundamentals/events.js)

---

## La consola más allá de `console.log`

El objeto `console` tiene más trucos de los que parece: medir tiempos con `console.time`/`timeEnd` y dibujar tablas con `console.table`. Pequeñas comodidades que hacen la depuración más agradable.

```javascript
--8<-- "learning/programming/node.js/fundamentals/cli.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/fundamentals/cli.js)

---

## Logs a fichero con un Console propio

¿Y si quieres que los logs vayan a un fichero en vez de a la pantalla? Puedes crear tu **propia** instancia de `Console` apuntando a streams de escritura: `stdout` y `stderr` separados.

```javascript
--8<-- "learning/programming/node.js/fundamentals/logger.js"
```

Aquí `fs.createWriteStream` abre dos ficheros (`stdout.log` y `stderr.log`), y el logger personalizado dirige `log()` a uno y `error()` al otro. Es la base de cualquier sistema de logging casero.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/fundamentals/logger.js)

---

## Interactividad: el juego de adivinar el número

Juntamos varias piezas en un mini-juego de terminal con el módulo `readline`: leemos la entrada del usuario línea a línea, mantenemos un estado (intentos restantes) y reaccionamos con eventos (`rl.on('line', ...)`). Tienes 3 intentos para adivinar un número del 1 al 10.

```javascript
--8<-- "learning/programming/node.js/fundamentals/game.js"
```

Es un ejemplo estupendo de cómo Node maneja la entrada interactiva de forma asíncrona: el programa no se "bloquea" esperando, sino que reacciona cada vez que escribes una línea y pulsas Enter.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/node.js/fundamentals/game.js)
