# Machine Learning con Python (IBM) 🔵

> **Material de terceros.** Notebooks del curso *Machine Learning with Python* de **IBM** (código `ML0101EN`, plataforma Cognitive Class). Los guardo aquí como referencia de estudio: es el cimiento "clásico" sobre el que descansa toda la serie de [Fundamentos del PLN y la IA](../fundamento-del-pln-y-la-ia.md) — antes de los transformers, había regresión y KNN.
>
> **Curso original:** [IBM · Machine Learning with Python (Cognitive Class)](https://cognitiveclass.ai/courses/machine-learning-with-python)

## Qué es

Un curso introductorio de IBM sobre aprendizaje automático con Python y `scikit-learn`. Recorre los algoritmos fundamentales con datasets pequeños y reproducibles. Los tres notebooks que conservo cubren:

- **Regresión lineal simple** (`ML0101EN-Reg-Simple-Linear-Regression-Co2-v2.ipynb`) — predecir emisiones de CO₂ a partir de una sola variable del motor.
- **Regresión lineal múltiple** (`ML0101EN-Reg-Mulitple-Linear-Regression-Co2-v2.ipynb`) — el mismo problema, ahora con varias variables predictoras.
- **K-Nearest Neighbors** (`ML0101EN-Clas-K-Nearest-neighbors-CustCat-v2.ipynb`) — clasificación de clientes en categorías según sus características.

El dataset estrella es `FuelConsumption.csv`, el clásico de consumo y emisiones de vehículos que aparece en medio internet de cursos de ML.

> [!NOTE]
> Estos notebooks **no son míos**: son material docente de IBM. Los incluyo como apuntes de estudio, no como trabajo original. El crédito es de IBM y sus autores.

## Por qué lo estudié

Porque los LLM no salieron de la nada. La intuición de **ajustar parámetros para minimizar un error** (regresión) y de **clasificar por cercanía** (KNN) es exactamente la base conceptual que luego escala —muchísimo— en redes neuronales y transformers. Hacer regresión lineal a mano una vez es lo que hace que después la frase "un modelo aprende pesos" deje de sonar a magia.

## Qué aprendí

- El flujo de trabajo de `scikit-learn`: `train_test_split` → `fit` → `predict` → métricas. Es el mismo esqueleto en casi todo el ML clásico.
- La diferencia práctica entre **regresión** (predecir un número, p. ej. emisiones) y **clasificación** (predecir una categoría, p. ej. tipo de cliente).
- Cómo evaluar honestamente: R², MAE/MSE para regresión; *accuracy* y matriz de confusión para KNN; y por qué el valor de **k** importa (sesgo vs. varianza).
- La importancia de **normalizar** las variables antes de un algoritmo basado en distancias como KNN.

## Cómo encaja en mi sitio

Es el "antes" de la era LLM. En la serie de historia del PLN cuento cómo la IA pasó de lo simbólico a lo estadístico y de ahí a lo neuronal; estos notebooks son la versión *hands-on* de ese capítulo estadístico. Quien venga de los fundamentos teóricos puede tocar aquí los algoritmos con sus propias manos.

> [!QUOTE] Crédito y origen
> Curso **"Machine Learning with Python" (ML0101EN)** de **IBM**, en la plataforma **Cognitive Class**.
> Autores originales: Saeed Aghabozorgi (IBM) y el equipo de Cognitive Class.
>
> - Curso original: <https://cognitiveclass.ai/courses/machine-learning-with-python>
> - Plataforma de aprendizaje: <https://apps.cognitiveclass.ai/learning/course/course-v1:BDU+ML0101EN+v4/home>
