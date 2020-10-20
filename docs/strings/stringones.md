# Stringones

En el idioma de la tribu de los *Stringones*, la mayoría de las palabras tienen muchas letras que se repiten de manera consecutiva. El sabio de la tribu ideó un sistema para escribir las palabras de manera abreviada: cada letra aparece antecedida de un número, indicando cuántas veces está repetida.

Por ejemplo, la palabra `pppprrrrrogggrraaa` se abrevia `4p5r1o3g2r3a`.

Desarrolle la función `original(abreviada)` que recibe como parámetro una palabra abreviada, y retorna la palabra original, antes de haber sido codificada. Suponga que ninguna letra aparece más de nueve veces seguidas.

## Ejemplo

```
>>> original('4p5r1o3g2r3a')
pppprrrrrogggrraaa
```

??? danger "Solución"
    ```python
    --8<-- "python/strings/stringones.py"
    ```