# Referencia: `prolog-examples` de Anne Ogborn 🔵

Una colección de ejemplos para programadores que empiezan en **programación lógica**, ideal para ver Prolog "en serio": rompecabezas, sistemas expertos, juegos y problemas de satisfacción de restricciones.

> [!NOTE]
> **Código de terceros.** Esta página _no_ reproduce el código; lo describe y enlaza al original. Guardo una copia en mi repositorio solo como material de estudio.

## Qué es

`prolog-examples` es un repositorio de **Anne Ogborn** (conocida en la comunidad como _Anniepoo_), una de las divulgadoras más activas de SWI‑Prolog. Reúne, en sus propias palabras, "algunos ejemplos sencillos para nuevos programadores de Prolog, con distintos grados de pulido". Es un cajón de sastre estupendo para estudiar **idioms** reales del lenguaje más allá del típico árbol genealógico.

Algunos de los ejemplos que más me interesaron:

- **Rompecabezas del detective** (`detectivepuzzle.pl`, `newdetective.pl`, `adriandetective.pl`): tres enfoques al mismo problema lógico —averiguar qué testimonio de los sospechosos es inconsistente—, incluyendo la solución de Adrian King. Perfecto para comparar un estilo "imperativo" frente a uno más declarativo.
- **`tictactoe.pl`**: el tres en raya completo.
- **`sudoku.pl`**: resolución de Sudoku con **CLP(FD)** (constraint logic programming sobre dominios finitos), donde declaras las restricciones y el motor encuentra la solución.
- **`expertsystem.pl`** y **`birds.pl`**: sistemas expertos sencillos (el de aves viene del tutorial "Expert Systems in Prolog" de Amzi).
- **`MonstersAndMazes.pl`** y **`roguelike.pl`**: lógica de juegos tipo mazmorra.
- **`cannibals2.pl`**: el clásico problema de misioneros y caníbales, muy bien comentado.
- **`talespin2.pl`**: implementación de un generador de historias clásico.
- **`pirates/`**: solución trabajada al tutorial de piratería de ClioPatria.
- Demos de **restricciones** (`addlists.pl`, `children.pl`, `constraintolist.pl`), de **cut** (`cuttutorial.pl`), de **DCG** (`dcgexample.pl`, `numbergrammar.pl`) y hasta de _sockets_ y lectura de CSV/Excel.

## Por qué lo estudié

Quería ver cómo se estructuran programas Prolog **no triviales**: cómo se modela un sistema experto, cómo se resuelve un puzzle con restricciones en vez de a fuerza bruta, y cómo el mismo problema (el detective) cambia de forma según lo "lógico" que sea tu enfoque. Es una referencia excelente para pasar de los hechos y reglas básicos a programas que de verdad _hacen_ algo.

## Cómo encaja

Complementa mis [ejercicios propios](ejercicios.md): donde los míos son mini‑demos de un concepto cada una, este repositorio muestra esos mismos conceptos —recursión, backtracking, restricciones— combinados en aplicaciones completas.

> [!QUOTE]
> **Crédito:** _prolog-examples_ © Anne Ogborn (Anniepoo). Publicado en su repositorio público de GitHub. Todo el mérito del código es suyo.

## Enlaces

- Repositorio original: <https://github.com/Anniepoo/prolog-examples>
