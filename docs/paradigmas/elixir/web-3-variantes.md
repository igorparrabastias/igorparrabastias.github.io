# "Hello World" web en Elixir: 3 capas, 3 niveles de abstracción

Una misma idea —responder `Hello, World!` por HTTP— resuelta de tres formas que comparten el mismo cimiento. Es la mejor manera de *ver* cómo se apilan las herramientas web del ecosistema BEAM y entender qué te da (y qué te cuesta) cada capa.

El paradigma funcional aparece aquí de un modo muy concreto: una petición HTTP es **un dato inmutable** (la `conn`) que fluye por una **tubería de funciones** que la van transformando hasta producir una respuesta. No hay un objeto `Request` mutable con efectos secundarios escondidos: hay transformaciones encadenadas con `|>`.

> [!TIP]
> Piensa en la `conn` como una bandeja que viaja por una cinta transportadora. Cada función le pone algo encima (un header, un status, un cuerpo) y la pasa a la siguiente. Al final, alguien la sirve. 🍽️

## El mapa de las tres capas

```
Cowboy   →  servidor HTTP de bajo nivel (Erlang). Tú gestionas todo.
  ⬇  (Plug se monta encima de Cowboy)
Plug     →  especificación + router minimalista. Composición de funciones.
  ⬇  (Phoenix se monta encima de Plug)
Phoenix  →  framework completo. Convenciones, MVC, sockets, vistas.
```

Lo importante: **no son tres mundos rivales, sino tres alturas de la misma montaña**. Phoenix usa Plug, y Plug usa Cowboy. Subes en abstracción a cambio de ceder control.

```
--8<-- "learning/programming/elixir/hello-world-elixir-web-app-in-3-variants/README.md"
```

## Variante 1 — Cowboy: el metal desnudo

Cowboy es el servidor HTTP en Erlang sobre el que todo lo demás se apoya. Trabajar directamente con él significa hablar su API (`:cowboy_req`, módulos en `erlang:`) y montar el router a mano. El `start/2` de la aplicación compila las rutas y arranca el servidor:

```elixir
--8<-- "learning/programming/elixir/hello-world-elixir-web-app-in-3-variants/variant-1-cowboy/lib/hello_world.ex"
```

Cada ruta apunta a un **handler**, un módulo con `init/2` que recibe la petición cruda y construye la respuesta llamando a `:cowboy_req.reply/4`:

```elixir
--8<-- "learning/programming/elixir/hello-world-elixir-web-app-in-3-variants/variant-1-cowboy/lib/hello_world/hello_handler.ex"
```

**Trade-off:** control total y mínima magia, a cambio de verbosidad y de hablar APIs de Erlang. Útil para entender qué ocurre por debajo; incómodo para una app real.

## Variante 2 — Plug: composición funcional pura

Plug es la pieza central del web en Elixir: una **especificación** de "cómo se ve una función que transforma una conexión". `Plug.Router` te da un DSL declarativo y, sobre todo, introduce la `conn` y el pipe `|>`. Mira cómo el router es legible casi como prosa:

```elixir
--8<-- "learning/programming/elixir/hello-world-elixir-web-app-in-3-variants/variant-2-plug/lib/hello_world/router.ex"
```

Fíjate en `plug :match` y `plug :dispatch`: la petición pasa por una **cadena de plugs** (incluido `Plug.Logger`). Y la respuesta se construye con una tubería: `conn |> put_resp_content_type(...) |> send_resp(...)`. Eso es el paradigma funcional aplicado al web: datos que fluyen por funciones.

**Trade-off:** el punto dulce para servicios pequeños y APIs ligeras. Mucho más ergonómico que Cowboy, sin el peso de un framework completo.

## Variante 3 — Phoenix: convenciones y batería incluida

Phoenix es el framework completo (MVC, sockets en tiempo real, vistas, i18n). Curiosamente, **por dentro sigue siendo Plug**: su `Endpoint` no es más que una pila de plugs que termina en el router. El router ahora separa *rutas* de *acciones de controlador*:

```elixir
--8<-- "learning/programming/elixir/hello-world-elixir-web-app-in-3-variants/variant-3-phoenix/web/router.ex"
```

Y la lógica vive en un controlador, una función `(conn, params) -> conn` — la misma forma funcional de siempre:

```elixir
--8<-- "learning/programming/elixir/hello-world-elixir-web-app-in-3-variants/variant-3-phoenix/web/controllers/hello_world_controller.ex"
```

**Trade-off:** máxima productividad y funcionalidad (live reload, parsers, sesiones, gettext…) a cambio de estructura, dependencias y curva de convenciones. Para un "Hello World" es exagerado; para una app de verdad, es donde quieres estar.

## Resumen comparativo

| | Cowboy | Plug | Phoenix |
|---|---|---|---|
| Nivel | Bajo (Erlang) | Medio | Alto |
| Router | Manual | DSL minimalista | DSL + scopes |
| Abstracción de petición | `:cowboy_req` crudo | `conn` + pipes | `conn` + MVC |
| Ideal para | Aprender / casos extremos | APIs y servicios ligeros | Apps completas |
| Coste | Verbosidad | Casi ninguno | Convenciones + deps |

La moraleja: **subir de capa nunca te aleja del paradigma**, solo te da más azúcar sobre la misma idea de funciones que transforman una conexión inmutable. 🧗

> [Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/elixir/hello-world-elixir-web-app-in-3-variants)
