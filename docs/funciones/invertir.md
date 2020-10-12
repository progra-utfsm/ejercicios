# Invertir número

Realice un programa que dado un $n$ de entrada haga lo siguiente:

- Cuente el número de dígitos
- Muestre el número invertido
- Indique si el número es capicúa, es decir, se lee igual de izquierda a derecha que de derecha a izquierda.

## Ejemplos

```
n: 0
Dígitos: 1
Invertido: 0
Es capicua
```

```
n: 1234
Dígitos: 4
Invertido: 4321
No es capicua
```

```
n: 123454321
Dígitos: 9
Invertido: 123454321
Es capicua
```

??? danger "Solución"
    ```python
    --8<-- "python/funciones/invertir.py"
    ```