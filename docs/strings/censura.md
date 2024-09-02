# Censura

Construya un algoritmo que reciba un texto compuesto únicamente de palabras separadas por espacios, y reemplace cada aparición de una palabra dentro del texto por un número de hashtags (#) igual al largo de la palabra censurada. La palabra no debe ser censurada cuando se encuentre dentro de otra (por ejemplo, "pollo" no debiese censurarse dentro de "repollo"). La censura no discrimina entre mayúsculas y minúsculas. Su algoritmo debe mostrar el texto modificado.

## Ejemplos

```
>>> Ingrese un texto: Un dia vi un unicornio
>>> Ingrese una palabra: perro
Un dia vi un unicornio
>>> Ingrese un texto: Un dia vi un unicornio
>>> Ingrese una palabra: UNICORNIO
Un dia vi un #########
>>> Ingrese un texto: Un dia vi un unicornio
>>> Ingrese una palabra: un
## dia vi ## unicornio
```

??? danger "Solución"
    ```python
    --8<-- "python/strings/censura.py"
    ```
