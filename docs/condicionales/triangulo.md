# Triángulo

Dados $3$ números reales que forman un triángulo debemos indicar qué tipo de triángulo es según sus lados y según sus ángulos.
Considerando $c$ como el lado de mayor longitud: 

- Si $a^2 + b^2 = c^2$ es rectángulo
- Si $a^2 + b^2 < c^2$ es obtusángulo 
- Si $a^2 + b^2 > c^2$ es acutángulo

Debe validar que el triángulo cumpla con la desigualdad triangular, esto es,

\begin{equation}
    (a + b) > c, \quad (a + c) > b, \quad (b + c) > a.
\end{equation}

??? danger "Solución"
    ```python
    --8<-- "python/condicionales/triangulo.py"
    ```