# Referencia: `Metro` de Dimiter Dobrev 🔵

Un proyecto ambicioso y poco común: una **simulación completa de metro** escrita en un dialecto de Prolog con ventana gráfica propia. Muestra hasta dónde puede llegar la **programación lógica** cuando se mezcla con estado y gráficos.

> [!NOTE]
> **Código de terceros.** Esta página describe y enlaza al original; no reproduce su código. Conservo una copia solo como material de estudio.

## Qué es

`Metro` es una simulación del movimiento de trenes de metro creada por **Dimiter Dobrev**, el autor de **Strawberry Prolog** (un intérprete de Prolog desarrollado en la Academia Búlgara de Ciencias y varias universidades de Sofía). El proyecto propone un nuevo esquema de circulación de vagones que —según su web— aumentaría la capacidad del túnel, reduciría el tiempo de viaje y bajaría el consumo eléctrico, y lo acompaña de una simulación visual para demostrarlo.

El código está repartido en varios archivos característicos de Strawberry Prolog:

- **`Metro.pro`** — el programa principal: incluye los demás módulos, define la lógica temporal de la simulación (`time_func/1`, agrupación de tiempos `in_group/1`, colores de vagones…) y abre la ventana gráfica.
- **`metro_map.h`**, **`metro_map1.h`**, **`metro_map2.h`**, **`metro_map3.h`** — distintos mapas/trazados de la red.
- **`metro_data.h`** — datos de la simulación.
- **`metro_window.h`** — toda la lógica de la ventana y el dibujado (el archivo más grande, con el renderizado).
- **`metro_tools.h`** — utilidades de apoyo.
- **`test.metro`** — un escenario de prueba que el programa puede cargar.

Llama la atención el estilo: usa asignación destructiva (`:=`), `include/1` para los módulos y un predicado `window(...)` para la GUI. Es Prolog, sí, pero con un sabor muy distinto al de SWI‑Prolog.

## Por qué lo estudié

Es el ejemplo más alejado del Prolog "de libro" que encontré: un sistema con **estado mutable, tiempo y gráficos** construido sobre un motor lógico. Me sirvió para ver un **dialecto** diferente (Strawberry Prolog frente a SWI‑Prolog) y para entender cómo se modela una simulación dinámica —algo intrínsecamente imperativo— dentro de un lenguaje declarativo. También es una curiosidad histórica interesante (las cabeceras citan una solicitud de patente de 2016).

## Cómo encaja

Cierra el recorrido por el paradigma mostrando su extremo más exótico. Si mis [ejercicios](ejercicios.md) son el Prolog mínimo y el [microservicio](ref-newton-microservice.md) es Prolog "de producción", `Metro` es Prolog llevado a un terreno gráfico y de simulación que poca gente asocia con la programación lógica.

> [!QUOTE]
> **Crédito:** _Metro_ © **Dimiter Dobrev** (dobrev.com), escrito en **Strawberry Prolog**. Todo el mérito del código es suyo. La versión 1.0 original se distribuyó en `http://dobrev.com/software/Metro_v1_0.zip`.

## Enlaces

- Sitio del autor / Strawberry Prolog: <https://dobrev.com/>
- Descarga original (v1.0): <http://dobrev.com/software/Metro_v1_0.zip>
