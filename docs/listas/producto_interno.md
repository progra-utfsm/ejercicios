# Producto Interno

Sean $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ dos vectores definidos como:

$$
\mathbf{u} = \left(u_1, u_2, \dots, u_n\right)^{\top}, \quad
\mathbf{v} = \left(v_1, v_2, \dots, v_n\right)^{\top}.
$$

El producto interno, escalar o punto se calcula de la siguiente forma:

$$
\mathbf{u}\cdot\mathbf{v} = u_1\,v_1 + u_2\,v_2 + \cdots + u_n\,v_n = 
\sum_{i=1}^nu_i\,v_i.
$$

Desarrolle la función `producto_interno(u, v)` que recibe dos listas que representan los vectores $\mathbf{u}$ y $\mathbf{v}$, y calcule el producto interno.

## Ejemplos
```
>>> producto_interno([1, 0], [0, 1])
0
>>> producto_interno([1, 2, 3], [4, 5, 6])
32
>>> producto_interno([0, -1, 2.3, 4, 99], [-1, 0, 0, 2, 2])
206.0
```


??? danger "Solución"
    ```python
    --8<-- "python/listas/producto_interno.py"
    ```

