# Desviación estándar

La desviación estándar es una medida que se usa para cuantificar la variación o dispersión de un conjunto de datos numéricos.

\begin{equation}
    \sigma = \sqrt{\sum_{i=1}^n \frac{(x_i-\mu)^2}{n-1}}
\end{equation}

Donde $n$ es la cantidad de datos, $\mu$ es el promedio y los $x_i$ son cada uno de los datos. Esto significa que hay que hacerlo siguiendo estos pasos:

- Calcular el promedio de los valores;
- a cada valor hay que restarle el promedio, y el resultado elevarlo al cuadrado;
- sumar todos los valores obtenidos;
- dividir la suma por la cantidad de valores; y
- sacar la raíz cuadrada del resultado.

Desarrolle la función `desviacion_estandar(valores)` cuyo parámetro `valores` sea una lista de números reales. La función debe retornar la desviación estándar de los valores.

## Ejemplos

```
>>> desviacion_estandar([1.3, 1.3, 1.3])
0.0
>>> desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0])
4.88535225615
>>> desviacion_estandar([1.5, 9.5])
5.65685424949
```

??? danger "Solución"
    ```python
    --8<-- ";python/listas/desviacion.py"
    ```