# Arquitectura y organización de computadores

Cómo funciona un computador **por dentro**, del bit a los núcleos. El título del curso encierra su propia distinción:

- **Arquitectura** = lo que *ve el programador*: el conjunto de instrucciones (ISA), los registros, los tipos de datos y los modos de direccionamiento. El **qué hace** la máquina.
- **Organización** = cómo se *implementa físicamente*: el camino de datos, las señales de control, los buses y la tecnología de memoria. El **cómo lo hace**.

> [!TIP]
> Dos procesadores pueden compartir la misma **arquitectura** (ejecutan el mismo código) y tener **organizaciones** muy distintas —uno barato y lento, otro caro y veloz—. Esa separación es justo lo que permite que tu programa de hace diez años siga corriendo en el chip de hoy. 🧩

<div class="grid cards" markdown>

-   :material-numeric: __Representación y lógica digital__

    ---

    Binario y complemento a dos, punto flotante IEEE 754, caracteres, y el álgebra
    de Boole con la que se construyen los circuitos.

    [:octicons-arrow-right-24: Entrar](representacion.md)

-   :material-chip: __CPU, ISA y ciclo de instrucción__

    ---

    El modelo von Neumann, la ALU y los registros, el ciclo buscar–decodificar–
    ejecutar, el conjunto de instrucciones y RISC vs CISC.

    [:octicons-arrow-right-24: Entrar](cpu.md)

-   :material-memory: __Jerarquía de memoria__

    ---

    Registros → caché → RAM → disco: localidad, mapeo de caché, aciertos y fallos,
    y memoria virtual con paginación.

    [:octicons-arrow-right-24: Entrar](memoria.md)

-   :material-swap-horizontal: __Entrada/salida y buses__

    ---

    Cómo habla la CPU con el mundo: E/S programada, por interrupciones y DMA, más
    la jerarquía de buses.

    [:octicons-arrow-right-24: Entrar](entrada-salida.md)

-   :material-speedometer: __Segmentación, rendimiento y paralelismo__

    ---

    Medir el rendimiento (CPI, ley de Amdahl), la segmentación y sus riesgos, y el
    paralelismo de datos e hilos hasta las GPUs.

    [:octicons-arrow-right-24: Entrar](paralelismo.md)

</div>
