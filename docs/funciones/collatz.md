# Conjetura de Collatz o Ulam

La conjetura de Collatz o Ulam es un famoso problema matemático aún sin resolver que afirma lo siguiente: tomando cualquier número entero positivo, si es par se lo divide entre 2, si es impar se lo multiplica por 3 y se le suma 1; repitiendo este proceso con el resultado, la secuencia siempre llegará eventualmente al número 1, sin importar el número inicial.

El enunciado formal es el siguiente: Definido para $n\in\mathbb{N}$,

$$
f(n) =
\begin{cases}
\frac{n}{2} & \text{si } n \text{ es par} \\
3n + 1 & \text{si } n \text{ es impar}
\end{cases}
$$

$$
a_{i} =
\begin{cases}
n & \text{para } i = 0 \\
f(a_{i-1}) & \text{para } i > 0
\end{cases}
$$
 
Realizando iteraciones sucesivas, el proceso termina en 1 para cualquier entero positivo inicial (según la conjetura).

Se solicita que realice un programa para implementar esta conjetura, con lo siguiente:
* Una función que retorne verdadero si un número es par y falso si no lo es.
* Una función que aplique la operación $n/2$ para $n$ par.
* Una función que aplique la operación $3n+1$ si $n$ es impar.
* Mostrar todos los valores de la secuencia hasta terminar en $1$.

Además, el programa debe determinar:
1. La cantidad de números pares que se generaron.
2. La cantidad de números impartes que se generaron.
3. El máximo valor obtenido.

## Ejemplos
```
Ingrese n: 10
10
5
16
8
4
2
1
Máximo: 16
Cantidad de pares: 5
Cantidad de impares: 2
```

```
Ingrese n: 100
100
50
25
76
38
19
58
29
88
44
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
Máximo: 88
Cantidad de pares: 18
Cantidad de impares: 8
```

??? danger "Solución"
    ```python
    --8<-- "python/funciones/collatz.py"
    ```