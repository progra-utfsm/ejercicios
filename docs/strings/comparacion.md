# Comparación

Escriba un programa que reciba dos strings a comparar y un nivel de tolerancia que es un número entero no negativo (cero o más). El programa debe mostrar si los strings son iguales ignorando diferencias hasta la cantidad de tolerancia indicada. Por ejemplo, "perro" y "perXo" son iguales para tolerancia 1, pero son distintos para tolerancia 0.

## Ejemplos

```
String 1: perro
String 2: perXo
Tolerancia: 1
Iguales con tolerancia = 1
```

```
String 1: perro
String 2: perXo
Tolerancia: 0
Distintos con tolerancia = 0
```

??? danger "Solución"
    ```python
    --8<-- "python/strings/comparacion.py"
    ```