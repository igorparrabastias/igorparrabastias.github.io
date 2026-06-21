# Referencia: `newton-microservice` de Daniel Schruhl 🔵

Un experimento delicioso: ¿y si montas un **microservicio web** entero… en Prolog? Este proyecto demuestra que la **programación lógica** no se queda en el aula y puede servir peticiones HTTP.

> [!NOTE]
> **Código de terceros.** Esta página describe y enlaza al original; no reproduce su código. Conservo una copia solo como material de estudio.

## Qué es

`newton-microservice` es un microservicio mínimo escrito en **SWI‑Prolog** por **Daniel Schruhl** (usuario _meandor_ en GitHub). Su objetivo, declarado en el README, es "hacer un microservicio sencillo en Prolog": arranca un servidor web usando las bibliotecas HTTP de SWI‑Prolog y responde a rutas que tú defines.

La arquitectura es minimalista y muy legible:

- **`core.pl`** — el arranque: carga `library(http/thread_httpd)` y `library(http/http_dispatch)`, consulta las rutas y predicados, y levanta el servidor en el puerto `8080`.
- **`routes.pl`** — define los _handlers_ HTTP (`http_handler('/', say_hi, [])`).
- **`predicates.pl`** — la lógica detrás de cada ruta (el clásico `Hello World!`).
- **`Dockerfile`** — empaqueta todo sobre una imagen con SWI‑Prolog y expone el puerto 8080, de modo que el servicio se ejecuta con un simple `docker run`.

Separar **rutas** de **predicados** deja claro el patrón: la URL se mapea a un predicado, y el predicado produce la respuesta. Sorprendentemente parecido a cualquier microframework web, pero en lógica pura.

## Por qué lo estudié

Me interesaba ver Prolog **fuera de su zona de confort**: no resolviendo puzzles, sino haciendo de backend HTTP. Es un recordatorio de que SWI‑Prolog trae un servidor web maduro de serie, y de lo poco que hace falta para exponer reglas lógicas como una API. La pieza del `Dockerfile` además muestra cómo desplegarlo de forma reproducible.

## Cómo encaja

Es el contrapunto "aplicado" a mis [ejercicios](ejercicios.md) y a los [ejemplos de Anne Ogborn](ref-prolog-examples.md): la prueba de que un motor de inferencia también puede vivir detrás de un endpoint y responder a peticiones del mundo real.

> [!QUOTE]
> **Crédito:** _newton-microservice_ — Licencia **MIT**, © 2016 **Daniel Schruhl** (`danielschruhl@gmail.com`). Todo el mérito del código es suyo.

## Enlaces

- Repositorio original: <https://github.com/meandor/newton-microservice>
