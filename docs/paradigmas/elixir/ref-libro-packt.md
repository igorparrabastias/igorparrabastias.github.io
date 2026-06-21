# 🔵 Referencia: código del libro "Learning Elixir" (Packt)

El *code bundle* oficial del libro **Learning Elixir** de Packt. Material de terceros que seguí para profundizar en concurrencia y OTP; lo dejo como referencia comentada, no como código propio.

## Qué es

Es el paquete de ejemplos que acompaña al libro **Learning Elixir** (Packt Publishing), escrito por **Kenny Ballou**. El libro está pensado para quien llega nuevo a Elixir —y a Erlang— con el objetivo de sentirse cómodo programando en estilo **funcional** y, a partir de ahí, construir aplicaciones más escalables y tolerantes a fallos.

El código está organizado por capítulos (`code/chapter2` … `code/chapter9`). Los capítulos que más trabajé caen en el rango 3–6 y son justamente los que conectan con el paradigma:

- **Capítulo 3** — fundamentos funcionales: recursión y módulos (`fibonacci_1.exs`, `fibonacci_2.exs`, `mymath_*.exs`, `sort.exs`, `reverse.exs`).
- **Capítulo 4** — estructuras y algoritmos sobre datos inmutables (`graph.exs`, `dag.exs`, `wordcount.exs`).
- **Capítulo 5** — más algoritmos clásicos (`fizzbuzz.exs`, `mergesort`).
- **Capítulo 6** — **concurrencia y procesos**: el grueso de lo interesante (`pingpong.exs`, `worker.exs`, `pmap.exs`, `fib_pool.exs`, `heartmon.exs`, `kv.exs`, `workpool`).

## Por qué lo estudié

El capítulo 6 es el puente directo con el resto de esta serie: `pingpong.exs` es la versión "de libro" del mismo experimento de procesos que tengo como [PingPong original](pingpong.md), y `pmap.exs`/`workpool` muestran cómo escalar ese modelo de mensajes a *pools* de workers —exactamente la idea de "tareas encoladas" que motivaba mis pruebas para APIs. Estudiarlo me dio el vocabulario de OTP (procesos, supervisión, pools) sobre una base sólida.

## Cómo encaja

Lo uso como **manual de referencia** del paradigma funcional y concurrente: cuando un patrón (mapeo paralelo, monitorización de procesos, almacén clave-valor con estado en un proceso) aparece en mis experimentos, el code bundle es donde voy a ver una implementación canónica explicada.

> [!NOTE]
> **Crédito.** Todo el código pertenece al libro **Learning Elixir**, de **Kenny Ballou**, publicado por **Packt Publishing**. Se distribuye bajo la **GNU General Public License v3 (GPLv3) o posterior**, tal y como indican su `README` y `LICENSE`. El mérito del contenido es del autor y la editorial; aquí solo lo referencio como material de estudio.

## Enlaces

- 📕 **Libro (editorial):** [Learning Elixir — Packt](https://www.packtpub.com/en-us/product/learning-elixir-9781785881749)
- ⚖️ **Licencia:** [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt)
