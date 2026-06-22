# Rendimiento

Hacer un computador más rápido no es solo subir la frecuencia del reloj. Antes de optimizar hay que saber **medir**, y aquí abundan los números engañosos.

## La fórmula honesta

La frecuencia (GHz) por sí sola miente: un chip más veloz puede ser más lento si necesita más ciclos por tarea. El tiempo real de CPU se descompone en tres factores:

> **tiempo = nº de instrucciones × CPI × tiempo de ciclo**

donde **CPI** es los *ciclos por instrucción* promedio. Mejorar el rendimiento es reducir cualquiera de los tres:

- menos **instrucciones** → mejor compilador o mejor algoritmo;
- menor **CPI** → mejor arquitectura (segmentación, ejecución fuera de orden);
- menor **tiempo de ciclo** → mejor tecnología de fabricación.

Lo interesante es que **se compensan entre sí**: un diseño RISC sube el número de instrucciones pero baja tanto el CPI y el ciclo que gana en conjunto.

## MIPS, FLOPS y por qué desconfiar

Medidas como **MIPS** (millones de instrucciones por segundo) o **FLOPS** (operaciones de coma flotante por segundo) resumen el ritmo en un solo número, pero hay que tomarlas con pinzas: no todas las instrucciones cuestan lo mismo, y dos máquinas con la misma cifra de MIPS pueden rendir muy distinto en un programa real. Por eso se usan **benchmarks** —programas representativos— en vez de fiarse de un número aislado.

## La ley de Amdahl

El aviso más importante de todo el tema: si solo una parte de un programa se puede acelerar, la mejora total tiene un **techo**. La **ley de Amdahl** lo formaliza —si el 80 % de un programa es paralelizable y el 20 % no, ni con infinitos núcleos bajarás de ese 20 % de tiempo—.

La moraleja es profunda: **la parte secuencial manda**. No basta con "añadir más núcleos"; si no se reduce la fracción que no se puede acelerar, el esfuerzo se topa con un muro. Es la razón por la que escalar el rendimiento es mucho más difícil de lo que parece.

---

➡️ Sigue en [Paralelismo](paralelismo.md).
