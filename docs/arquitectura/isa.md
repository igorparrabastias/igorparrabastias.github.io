# Conjunto de instrucciones (ISA)

La **ISA** (*Instruction Set Architecture*) es el **contrato entre el hardware y el software**: define todo lo que un programa puede pedirle a la CPU. Es, justamente, la frontera que da nombre a la *arquitectura* —lo que ve el programador— frente a la *organización* —cómo se implementa por dentro—. Por eso dos chips muy distintos pueden ejecutar el mismo programa si comparten la ISA.

## Qué define una ISA

- El **repertorio de instrucciones**: aritméticas (sumar, multiplicar), de movimiento de datos (cargar, almacenar), lógicas, de control de flujo (saltos, llamadas) y de E/S.
- Los **registros** disponibles y su tamaño (la "anchura" de la máquina: 32 o 64 bits).
- Los **formatos de instrucción**: cómo se empaquetan en binario el código de operación (*opcode*) y los operandos.
- Los **modos de direccionamiento**.

## Modos de direccionamiento

Una instrucción necesita decir *dónde* están sus datos, y hay varias formas de indicarlo:

- **Inmediato**: el dato viaja dentro de la propia instrucción (`suma 5`).
- **Directo**: la instrucción trae la dirección de memoria del dato.
- **De registro**: el dato está en un registro.
- **Indirecto**: la instrucción apunta a un lugar que, a su vez, contiene la dirección del dato (la base de los punteros).
- **Indexado**: dirección base + un desplazamiento de un registro índice (ideal para recorrer arreglos).

Esta variedad es lo que permite a un lenguaje de alto nivel traducir punteros, arreglos y estructuras a algo que la máquina entienda.

## RISC vs CISC

Hay dos grandes filosofías de diseño:

- **CISC** (p. ej. x86): muchas instrucciones, algunas **complejas** que hacen mucho en una sola orden. El código ocupa menos, pero el hardware es más complicado y difícil de acelerar.
- **RISC** (p. ej. ARM, RISC-V): pocas instrucciones **simples y regulares**, fáciles de segmentar y de ejecutar en un ciclo. Necesita más instrucciones por tarea, pero corre más rápido y gasta menos energía. Domina hoy en móviles y, cada vez más, en todas partes (incluidos los chips de Apple y los servidores).

## Ensamblador

Programar en **ensamblador** es escribir directamente en este nivel: una línea por instrucción, usando nombres mnemotécnicos (`MOV`, `ADD`, `JMP`) en vez de binario. Casi nadie programa así hoy, pero **leerlo** es esencial para entender qué hace de verdad el compilador, depurar a bajo nivel y optimizar lo crítico.

---

➡️ Sigue en [Segmentación (pipelining)](segmentacion.md).
