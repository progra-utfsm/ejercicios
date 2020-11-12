# Rectas

Una recta en el plano está descrita por la ecuación:

\begin{equation}
    y = mx+b,
\end{equation}

donde $m$ es la pendiente y $b$ es el intercepto. Todos los puntos de la recta satisfacen esta ecuación.

En un programa, una recta puede ser representada como una tupla `(m, b)`.

Los algoritmos para resolver los siguientes ejercicios seguramente usted los aprendió en el colegio. 
Si no los recuerda, puede buscarlos en su libro de matemáticas favorito o en internet.

## Ejercicio 1

Escriba la función `punto_en_recta(p, r)` que indique si el punto `p` está en la recta `r`:

### Ejemplos

```
>>> recta = (2, -1)     # esta es la recta y = 2x - 1
>>> punto_en_recta((2, 3), recta)
True
>>> punto_en_recta((0, -1), recta)
True
>>> punto_en_recta((1, 2), recta)
False
```

## Ejercicio 2

Escriba la función `son_paralelas(r1, r2)` que indique si las rectas `r1` y `r2` son paralelas, es decir, no se intersectan en ningún punto.

## Ejercicio 3

Escriba la función `recta_que_pasa_por(p1, p2)` que entregue la recta que pasa por los puntos `p1` y `p2`:

### Ejemplos

```
>>> recta_que_pasa_por((-2, 4), (4, 1))
(-0.5, 3.0)
```

Puede comprobar que la función está correcta verificando que ambos puntos están en la recta obtenida:

```
>>> p1 = (-2, 4)
>>> p2 = (4, 1)
>>> r = recta_que_pasa_por(p1, p2)
>>> punto_en_recta(p1, r) and punto_en_recta(p2, r)
True
```

## Ejercicio 4

Escriba la función `punto_de_interseccion(r1, r2)` que entregue el punto donde las dos rectas se intersectan. 
Si las rectas son paralelas, la función debe retornar `None`.

### Ejemplos

```
>>> r1 = (2, 1)
>>> r2 = (-1, 4)
>>> punto_de_interseccion(r1, r2)
(1.0, 3.0)
```

??? danger "Solución"
    ```python
    --8<-- "python/tuplas/rectas.py"
    ```