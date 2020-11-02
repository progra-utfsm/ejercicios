# Merge

Escribir la función `merge(lista1, lista2)` que recibe como parámetros dos listas de números que se encuentran ordenadas
ascendentemente. La función debe retornar una nueva lista ordenada que contiene la mezcla de las dos listas pasadas como
parámetro. La idea es aprovechar el orden de las listas de entrada, es decir, no basta con concatenarlas y ordenar el
resultado. Esto se puede pensar como la mezcla de dos barajas de cartas que ya están ordenadas. Claramente preferiremos
aprovechar el orden antes que simplemente juntarlas y ordenarlas de nuevo.

## Ejemplo

```
>>> l1 = [1, 1, 2, 3, 5, 6, 10, 12]
>>> l2 = [0, 2, 5, 5, 7, 8]
>>> merge(l1, l2)
[0, 1, 1, 2, 2, 3, 5, 5, 5, 6, 7, 8, 10, 12]
```

??? danger "Solución"
    ```python
    --8<-- ";python/listas/merge.py"
    ```