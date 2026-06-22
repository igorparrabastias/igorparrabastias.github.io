# Representación y lógica digital

Todo lo que un computador almacena —números, texto, imágenes, instrucciones— es, en el fondo, **bits**: ceros y unos. Esta página cubre cómo se codifica la información y cómo, con simple lógica, esos bits se convierten en circuitos que calculan.

## Sistemas de numeración

Usamos base 10 por tener diez dedos; la máquina usa **base 2** porque un transistor solo distingue dos estados (encendido/apagado). El **hexadecimal** (base 16) y el **octal** (base 8) son atajos para escribir binario de forma compacta: un dígito hex equivale a 4 bits, así que `1111 1010` se escribe `FA`.

## Enteros: el complemento a dos

Representar números positivos en binario es directo. El problema es el signo. La solución que usan casi todos los computadores es el **complemento a dos**: el bit más significativo pesa en negativo. Su gran virtud es que **la resta se vuelve una suma**: `A − B` se calcula sumando `A` con el complemento a dos de `B`, así que el mismo circuito sumador sirve para ambas operaciones. Con *n* bits se cubre el rango de −2ⁿ⁻¹ a 2ⁿ⁻¹−1 (por eso un entero de 8 bits va de −128 a 127), y el **desbordamiento** (*overflow*) ocurre cuando el resultado se sale de ese rango.

## Punto flotante (IEEE 754)

Para los números reales (con decimales) se usa el estándar **IEEE 754**, que guarda tres piezas, como la notación científica: **signo**, **exponente** y **mantisa** (los dígitos significativos). La **precisión simple** usa 32 bits; la **doble**, 64. Esto explica una rareza famosa: `0.1 + 0.2` no da exactamente `0.3`, porque 0,1 no tiene representación binaria finita —igual que 1/3 no la tiene en decimal—. De ahí que comparar flotantes con `==` sea mala idea.

## Caracteres

El texto también son números. **ASCII** asignaba 7 bits a cada carácter (suficiente para el inglés). Hoy reina **Unicode**, que da un número a cada símbolo de (casi) todos los idiomas y emojis, normalmente codificado en **UTF-8**, un esquema de longitud variable compatible con ASCII.

## Lógica digital

Aquí los bits se vuelven hardware. El **álgebra de Boole** opera sobre `verdadero/falso` con tres operaciones básicas —**AND, OR, NOT**— de las que derivan las demás (NAND, NOR, XOR). Cada una se implementa como una **puerta lógica**, un pequeño circuito de transistores.

- **Circuitos combinacionales**: la salida depende solo de las entradas actuales. Combinando puertas se construyen bloques útiles: un **sumador** (que implementa la aritmética de arriba), un **multiplexor** (selector), un **decodificador**.
- **Circuitos secuenciales**: tienen **memoria**; la salida depende también del estado anterior. El ladrillo es el **flip-flop**, que guarda un bit, y de ahí salen los **registros** y los contadores. Un **reloj** marca el ritmo al que el estado avanza.

Con estas dos familias —lógica que calcula y lógica que recuerda— ya se tiene todo lo necesario para construir una CPU.

---

➡️ Sigue en [CPU, ISA y ciclo de instrucción](cpu.md).
