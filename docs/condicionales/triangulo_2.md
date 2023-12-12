# Triángulos

Los tres lados $a$, $b$ y $c$ de un triángulo deben satisfacer la desigualdad triangular: En todo triángulo la suma de las longitudes de dos lados cualesquiera es siempre mayor a la longitud del lado restante. Definido matemáticamente, cualquier triángulo cumple la siguiente propiedad:

\begin{equation}
    a < (b + c), \quad b < (a + c), \quad c < (a + b).
\end{equation}

Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
- si acaso el triángulo es inválido; y
- si no lo es, qué tipo de triángulo es.

```
Ingrese a: 3.9
Ingrese b: 6.0
Ingrese c: 1.2
No es un triangulo valido.
```

```
Ingrese a: 1.9
Ingrese b: 2
Ingrese c: 2
El triangulo es isoceles.
```

```
Ingrese a: 3.0
Ingrese b: 5.0
Ingrese c: 4.0
El triangulo es escaleno.
```

??? danger "Solución"
    ```python
    --8<-- "python/condicionales/triangulos.py"
    ```