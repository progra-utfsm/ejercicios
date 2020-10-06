# Aproximación exponencial

Realice un programa que aproxime la función $e^x$ utilizando Serie de Taylor:

\begin{equation}
    e^x \approx \sum_{n=0}^N \dfrac{x^n}{n!}, \quad \forall x\in \mathbb{R}, n \in \mathbb{N}_0,
\end{equation}

donde $x$ y $N$ son entradas del programa.

??? danger "Solución"
    ```python
    --8<-- ";python/funciones/exponencial.py"
    ```