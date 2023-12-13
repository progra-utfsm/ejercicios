# Triángulo

Dados $3$ números reales que forman un triángulo debemos indicar qué tipo de triángulo es según sus lados (equilátero, isósceles o escaleno) y según sus ángulos.
Considerando $c$ como el lado de mayor longitud: 

- Si $a^2 + b^2 = c^2$ es rectángulo
- Si $a^2 + b^2 < c^2$ es obtusángulo 
- Si $a^2 + b^2 > c^2$ es acutángulo

Debe validar que el triángulo cumpla con la desigualdad triangular, esto es,

\begin{equation}
    (a + b) > c, \quad (a + c) > b, \quad (b + c) > a.
\end{equation}

## Ejemplos

```
Ingrese a: 3.9
Ingrese b: 6.0
Ingrese c: 1.2
No es un triángulo válido.
```

```
Ingrese a: 2.0
Ingrese b: 1.9
Ingrese c: 2.0
El triángulo es isósceles.
Además es acutángulo.
```

```
Ingrese a: 3.0
Ingrese b: 5.0
Ingrese c: 4.0
El triángulo es escaleno.
Además es rectángulo.
```

```
Ingrese a: 3.14
Ingrese b: 3.14
Ingrese c: 3.14
El triángulo es equilatero.
Además es acutángulo.
```


??? danger "Solución"
    ```python
    --8<-- "python/condicionales/triangulo.py"
    ```