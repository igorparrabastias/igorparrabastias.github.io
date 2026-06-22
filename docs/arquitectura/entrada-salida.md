# Entrada/salida y buses

Una CPU que solo calcula no sirve de nada: necesita **hablar con el mundo** —teclado, disco, red, pantalla—. Esta página trata cómo se coordina ese diálogo y por dónde circulan los datos.

## El problema de la E/S

Los dispositivos son **muchísimo más lentos** que la CPU y muy distintos entre sí. Para no atarse a cada uno, la CPU no habla directamente con el hardware sino con **módulos de E/S** (controladores) que exponen un puñado de registros. Acceder a esos registros se hace de dos maneras: **mapeada en memoria** (los registros del dispositivo ocupan direcciones como si fueran RAM, y se leen/escriben con las instrucciones normales) o con **E/S aislada** (instrucciones especiales y un espacio de direcciones aparte).

## Las tres técnicas

¿Cómo espera la CPU a un dispositivo lento? Hay tres enfoques, de peor a mejor aprovechamiento:

1. **E/S programada (*polling*)**: la CPU pregunta una y otra vez "¿ya estás listo?". Simple, pero **desperdicia** todo ese tiempo girando en vacío.
2. **Por interrupciones**: la CPU sigue con otro trabajo y el dispositivo **avisa** (lanza una *interrupción*) cuando termina. La CPU suspende lo que hacía, atiende con una rutina (*ISR*) y vuelve. Mucho más eficiente. Las interrupciones tienen **prioridades** y un **vector** que indica qué rutina ejecutar.
3. **DMA (acceso directo a memoria)**: para transferencias grandes (un bloque de disco entero), un controlador especial mueve los datos **entre el dispositivo y la RAM sin pasar por la CPU**, que solo se entera al final con una interrupción. Libera por completo al procesador.

## Buses

Un **bus** es el conjunto de cables compartidos por los que viajan los datos entre componentes. Clásicamente se distinguen tres:

- **Bus de datos**: lleva la información en sí.
- **Bus de direcciones**: indica *de/hacia dónde* (qué posición de memoria o dispositivo). Su ancho fija cuánta memoria se puede direccionar.
- **Bus de control**: las señales de coordinación (lectura/escritura, reloj, interrupciones).

Como un único bus para todo sería un cuello de botella, los computadores usan una **jerarquía de buses**: uno rápido y corto junto a la CPU y la memoria, y otros más lentos para los periféricos. En la práctica conoces sus nombres comerciales: **PCIe** para tarjetas gráficas y SSD veloces, **USB** para periféricos, **SATA** para discos.

---

➡️ Sigue en [Segmentación, rendimiento y paralelismo](paralelismo.md).
