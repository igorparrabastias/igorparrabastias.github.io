# Segmentación, rendimiento y paralelismo

Hacer un computador más rápido no es solo subir la frecuencia del reloj. Esta página trata cómo se **mide** el rendimiento y los grandes trucos para **exprimirlo**: solapar trabajo y hacer muchas cosas a la vez.

## Medir el rendimiento

La frecuencia (GHz) engaña: un chip más veloz puede ser más lento si necesita más ciclos por tarea. La fórmula honesta del tiempo de CPU es:

> **tiempo = nº de instrucciones × CPI × tiempo de ciclo**

donde **CPI** es los *ciclos por instrucción* promedio. Mejorar el rendimiento es reducir cualquiera de los tres factores (mejor compilador, mejor arquitectura, mejor tecnología). Medidas como **MIPS** o los **FLOPS** resumen el ritmo, pero hay que tomarlas con cuidado.

### La ley de Amdahl

Un aviso fundamental: si solo una parte de un programa se puede acelerar, la mejora total tiene un techo. La **ley de Amdahl** lo formaliza —si el 80 % es paralelizable y el 20 % no, ni con infinitos núcleos bajarás de ese 20 %—. Moraleja: **la parte secuencial manda**, y por eso no basta con "añadir más núcleos".

## Segmentación (*pipelining*)

La idea es la de una **línea de montaje**. En vez de ejecutar una instrucción de principio a fin antes de empezar la siguiente, se divide el ciclo en etapas (buscar, decodificar, ejecutar, memoria, escribir) y, en cada momento, hay **una instrucción distinta en cada etapa**. No acelera una instrucción suelta, pero multiplica el **caudal** (instrucciones terminadas por unidad de tiempo).

El problema son los **riesgos** (*hazards*), situaciones que rompen el flujo:

- **Estructurales**: dos instrucciones quieren el mismo recurso a la vez.
- **De datos**: una instrucción necesita un resultado que la anterior aún no terminó. Se mitigan con **adelantamiento** (*forwarding*) o, si no hay más remedio, con una **burbuja** (*stall*).
- **De control**: tras un salto, no se sabe qué instrucción viene. Se ataca con **predicción de saltos**: el procesador apuesta por el camino más probable y, si falla, descarta el trabajo especulado.

Llevar esto más lejos —ejecutar **varias instrucciones por ciclo**— es el diseño **superescalar**, que explota el *paralelismo a nivel de instrucción* (ILP).

## Paralelismo de verdad

Cuando una sola CPU no da más, se replica el trabajo:

- **SIMD** (*una instrucción, muchos datos*): una misma operación se aplica a un vector entero de valores de golpe. Ideal para gráficos, audio y álgebra.
- **Multinúcleo**: varios procesadores completos en un mismo chip, ejecutando hilos en paralelo (paralelismo a nivel de hilo).
- **GPUs**: llevan el SIMD al extremo con miles de núcleos simples. Son máquinas de multiplicar matrices en masa —justo lo que necesita el [cómputo de la IA](../matematicas/necesita-ia.md#4--cómputo-cloud-computing--el-músculo)—, por eso pasaron de los videojuegos a entrenar los modelos más grandes.

---

⬅️ Volver al [índice de la sección](index.md).
