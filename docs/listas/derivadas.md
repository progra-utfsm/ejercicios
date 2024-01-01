# Aproximación de derivadas

Podemos aproximar la derivada de una función utilizando el método denominado *Diferencias Finitas*. Este método se puede obtener utilizando una expansión en *Series de Taylor* de una función $f$ respecto a un punto cercano. Considerando una discretización de $N$ puntos sobre la variable $x\in[x_{\text{min}}, x_{\text{max}}]$, definimos

$$
x_i = x_{\text{min}} + i \Delta x, \quad i=0, 1, \dots, N-1, \quad  \Delta x = \dfrac{x_{\text{max}} - x_{\text{min}}}{N - 1}.
$$

Ahora, definiremos $f_i$ como la aproximación de la función $f$ en el punto $x=x_i$, es decir, $f_i = f(x_i)$.

Podemos aproximar la derivada de la función $f$ en el punto $x_i$, o sea $f'_i=f'(x_i)$, de las siguientes $3$ maneras:

* Diferencia finita **adelantada**

$$f'_i \approx \dfrac{f_{i+1} - f_i}{\Delta x}$$

* Diferencia finita **atrasada**

$$f'_i \approx \dfrac{f_{i} - f_{i-1}}{\Delta x}$$

* Diferencia finita **central**

$$f'_i \approx \dfrac{f_{i+1} - f_{i-1}}{2\Delta x} $$

Realice un programa que solicite:

1. El dominio de $x$, es decir, $x_{\text{min}}$ y $x_{\text{max}}$. 
2. La cantidad de puntos de discretización $N$.
3. El tipo de aproximación, o sea, si es *adelantada*, *atrasada* o *central*.

Y calcule la derivada de la función. El programa debe mostrar el error entre la derivada real y su aproximación. Para esto utilizaremos la norma $L-2$ o distancia euclideana de la siguiente forma:

$$
\text{Error} = \sqrt{\sum_{i=inicio}^{fin}(f_i-f'_i)^2},
$$

donde $inicio$ y $fin$ dependerá de el tipo de aproximación que esté utilizando.

La función de prueba que utilizaremos será: $f(x) = x \sin (x)$.

## Ejemplos

```
x min: 0
x max: 5
N: 32
Tipo: atrasada
Error: 1.1242595459725062
```
```
x min: 0
x max: 5
N: 32
Tipo: central
Error: 0.07297275585321655
```
```
x min: 0
x max: 5
N: 64
Tipo: adelantada
Error: 0.7766862915195681
```
```
x min: 0
x max: 5
N: 64
Tipo: central
Error: 0.025254054492286914
```


??? danger "Solución"
    ```python
    --8<-- "python/listas/derivadas.py"
    ```