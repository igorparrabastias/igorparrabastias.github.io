# Arquitectura y organización de computadores

Cómo funciona un computador **por dentro**, del bit a los núcleos. El título del curso encierra su propia distinción:

- **Arquitectura** = lo que *ve el programador*: el conjunto de instrucciones (ISA), los registros, los tipos de datos y los modos de direccionamiento. El **qué hace** la máquina.
- **Organización** = cómo se *implementa físicamente*: el camino de datos, las señales de control, los buses y la tecnología de memoria. El **cómo lo hace**.

> [!TIP]
> Dos procesadores pueden compartir la misma **arquitectura** (ejecutan el mismo código) y tener **organizaciones** muy distintas —uno barato y lento, otro caro y veloz—. Esa separación es justo lo que permite que tu programa de hace diez años siga corriendo en el chip de hoy. 🧩

<div class="grid cards" markdown>

-   :material-numeric: __Representación de la información__

    ---

    Binario, hexadecimal, complemento a dos, punto flotante IEEE 754 y la
    codificación del texto (ASCII/Unicode).

    [:octicons-arrow-right-24: Entrar](representacion.md)

-   :material-gate-and: __Lógica digital__

    ---

    Álgebra de Boole, puertas lógicas y los circuitos combinacionales y
    secuenciales (flip-flops) con los que se construye todo.

    [:octicons-arrow-right-24: Entrar](logica-digital.md)

-   :material-sync: __Modelo von Neumann y ciclo de instrucción__

    ---

    El programa almacenado, sus componentes, el cuello de botella y el ciclo
    buscar → decodificar → ejecutar.

    [:octicons-arrow-right-24: Entrar](von-neumann.md)

-   :material-chip: __La CPU__

    ---

    La ALU, el banco de registros y la unidad de control (cableada vs
    microprogramada), unidos por el camino de datos.

    [:octicons-arrow-right-24: Entrar](cpu.md)

-   :material-code-braces: __Conjunto de instrucciones (ISA)__

    ---

    El contrato hardware–software: modos de direccionamiento, RISC vs CISC y el
    ensamblador.

    [:octicons-arrow-right-24: Entrar](isa.md)

-   :material-view-sequential: __Segmentación (pipelining)__

    ---

    Solapar instrucciones como una línea de montaje, sus riesgos (*hazards*) y el
    paralelismo a nivel de instrucción.

    [:octicons-arrow-right-24: Entrar](segmentacion.md)

-   :material-memory: __Jerarquía de memoria__

    ---

    Registros → caché → RAM → disco: localidad, mapeo de caché, aciertos y fallos,
    y memoria virtual con paginación.

    [:octicons-arrow-right-24: Entrar](memoria.md)

-   :material-swap-horizontal: __Entrada/salida__

    ---

    Cómo habla la CPU con el mundo: E/S programada, por interrupciones y DMA, más
    la jerarquía de buses.

    [:octicons-arrow-right-24: Entrar](entrada-salida.md)

-   :material-speedometer: __Rendimiento__

    ---

    Medir de verdad: la fórmula del tiempo de CPU, el CPI, los MIPS y la ley de
    Amdahl.

    [:octicons-arrow-right-24: Entrar](rendimiento.md)

-   :material-arrow-split-vertical: __Paralelismo__

    ---

    Hacer varias cosas a la vez: SIMD, multinúcleo y el paralelismo masivo de las
    GPUs.

    [:octicons-arrow-right-24: Entrar](paralelismo.md)

</div>
