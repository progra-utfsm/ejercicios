# Aproximación exponencial

Realice un programa que aproxime la función $e^x$ utilizando Series de Taylor:

\begin{equation}
    e^x \approx \sum_{n=0}^N \dfrac{x^n}{n!}, \quad \forall x\in \mathbb{R}, n \in \mathbb{N}_0,
\end{equation}

donde $x$ y $N$ son entradas del programa.

## Ejemplos

```
Ingrese N: 10
Ingrese x: 1
Valor aproximacion: 2.7182818011463845
```

```
Ingrese N: 100
Ingrese x: 1
Valor aproximacion: 2.7182818284590455
```

```
Ingrese N: 100
Ingrese x: 2
Valor aproximacion: 7.389056098930649
```

??? danger "Solución"
    ```python
    --8<-- "python/ciclos/exponencial.py"
    ```