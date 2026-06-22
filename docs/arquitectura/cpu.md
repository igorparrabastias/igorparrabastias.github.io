# CPU, ISA y ciclo de instrucción

La unidad central de proceso es el cerebro de la máquina. Esta página explica su modelo, sus piezas y el latido que repite miles de millones de veces por segundo.

## El modelo von Neumann

Casi todos los computadores siguen la **arquitectura de von Neumann**: una **misma memoria** guarda tanto los **datos** como las **instrucciones** del programa. Es lo que hace al computador *programable* —cambiar de tarea es solo cargar otras instrucciones—, pero tiene un precio: como instrucciones y datos viajan por el mismo canal, este se satura. Es el famoso **cuello de botella de von Neumann**, y buena parte de la jerarquía de memoria y la caché existen para mitigarlo.

## Las piezas de la CPU

- **ALU** (unidad aritmético-lógica): hace las cuentas y las operaciones lógicas.
- **Banco de registros**: un puñado de celdas de memoria ultrarrápidas dentro de la CPU, donde viven los datos con los que se está trabajando ahora mismo.
- **Unidad de control**: orquesta todo, generando las señales que dicen a cada parte qué hacer en cada ciclo.
- **Registros especiales**: el **PC** (*program counter*) apunta a la siguiente instrucción; el **IR** (*instruction register*) guarda la instrucción que se está ejecutando.

## El ciclo de instrucción

El motor de todo es un bucle simple que se repite sin parar:

1. **Buscar** (*fetch*): traer de memoria la instrucción a la que apunta el PC.
2. **Decodificar** (*decode*): la unidad de control interpreta qué pide esa instrucción.
3. **Ejecutar** (*execute*): la ALU (u otra unidad) la realiza.
4. **Escribir** (*write-back*): guardar el resultado en un registro o en memoria, y avanzar el PC.

Al recorrido físico que siguen los datos entre registros, ALU y memoria durante este ciclo se le llama **camino de datos** (*datapath*); la unidad de control es quien abre y cierra las "compuertas" de ese camino en el orden correcto.

## El conjunto de instrucciones (ISA)

La **ISA** es el contrato entre el hardware y el software: el repertorio de instrucciones que la CPU entiende (sumar, cargar, saltar…), los registros disponibles y los **modos de direccionamiento** (cómo se indica dónde está un dato: inmediato, directo, indirecto, indexado…). Programar en **ensamblador** es escribir directamente en este nivel, una instrucción por línea.

Hay dos grandes filosofías:

- **CISC** (p. ej. x86): muchas instrucciones, algunas complejas que hacen mucho en una sola orden. Código más corto, hardware más complicado.
- **RISC** (p. ej. ARM, RISC-V): pocas instrucciones simples y regulares, fáciles de segmentar y de ejecutar rápido. Domina hoy en móviles y, cada vez más, en todas partes.

## Unidad de control: cableada vs microprogramada

¿Cómo genera la unidad de control sus señales? De dos formas: **cableada** (un circuito lógico fijo, muy rápido, típico de RISC) o **microprogramada** (cada instrucción se traduce a una secuencia de "microinstrucciones" guardadas en una pequeña memoria interna, más flexible, típico de CISC).

---

➡️ Sigue en [Jerarquía de memoria](memoria.md).
