# Método de Newton

El **método de Newton** es un algoritmo para encontrar aproximaciones de los ceros o raíces de una función real.

\begin{equation}
    x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}
\end{equation}

Calcule $\sqrt{2}$, sabiendo que $f(x)=x^2−2$, $f'(x)=2x$. El número máximo de iteraciones $N$ y $x_0$ son entradas del programa.

??? danger "Solución"
    ```python
    --8<-- "python/funciones/newton.py"
    ```