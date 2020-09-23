# Calculadora

Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
El programa debe recibir como entrada $2$ números enteros y un operador, que puede ser `+`, `-`, `*` o `/`.
La salida del programa debe ser el resultado de la operación.

## Ejemplos

```
Operando: 3
Operador: +
Operando: 2
3 + 2 = 5
```

```
Operando: 6
Operador: -
Operando: 7
6 - 7 = -1
```

```
Operando: 4
Operador: *
Operando: 5
4 * 5 = 20
```

```
Operando: 10
Operador: /
Operando: 4
10 / 4 = 2.5
``` 

??? danger "Solución"
    ```python
    --8<-- "python/condicionales/calculadora.py"
    ```