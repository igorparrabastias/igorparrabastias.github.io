# FizzBuzz en PHP (y un saludo en JS)

Un clásico entre los clásicos. **FizzBuzz** es a la vez un juego infantil para enseñar divisiones y el filtro de entrevista más famoso del mundo del software: si alguien no logra escribirlo, probablemente no sepa programar. Aquí está mi versión en **PHP**.

Todo el código embebido es **código real** del laboratorio. Si tocas el archivo fuente, esta página se actualiza sola.

> [!TIP]
> Dato curioso: FizzBuzz se hizo famoso como pregunta de entrevista precisamente porque es *trivial*... y aun así mucha gente fallaba. La moraleja no es el algoritmo, es no asumir nada. 🙃

---

## FizzBuzz en PHP

La consigna habitual: cuenta números y sustituye los divisibles por 3 por "fizz", los divisibles por 5 por "buzz" y los divisibles por ambos por "fizzbuzz". Esta variante hace un giro divertido: en vez de imprimir los 100 primeros números, **acumula los 100 primeros múltiplos de 15** (los que serían "fizzbuzz") y los vuelca con `var_dump`.

```php
--8<-- "learning/programming/php/fizzbuzz.php"
```

Detalles a observar: las funciones `div3` / `div5` usan el operador de comparación estricta (`===`) sobre el resto (`%`), y el bucle `do...while` sigue iterando hasta que el acumulador llega a 100 elementos. Es PHP a la vieja usanza, directo y sin ceremonias.

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/php/fizzbuzz.php)

---

## Snippets sueltos

Pequeños fragmentos que no merecen página propia pero que vale la pena tener a mano.

### El "Hola mundo" más honesto (JavaScript)

De los *workshoppers* de aprendizaje, el primer programa de todos: el saludo de rigor. Un recordatorio de que toda gran torre empieza por una sola línea.

```javascript
--8<-- "learning/programming/js/workshoppers/hello.js"
```

[Ver en GitHub](https://github.com/igorparrabastias/igorparrabastias.github.io/blob/main/learning/programming/js/workshoppers/hello.js)
