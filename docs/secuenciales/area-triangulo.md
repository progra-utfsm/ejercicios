# Área Triángulo

Realice un programa que calcule el área de un triángulo a partir de las longitudes de sus lados. Para calcularlo utilice la fórmula de Herón:

\begin{equation}
    A = \sqrt{s\,(s-a)(s-b)(s-c)}
\end{equation}

donde $a$, $b$ y $c$ son las longitudes de cada lado y $s=\dfrac{a+b+c}{2}$ es el semiperímetro.

??? danger "Solución"
    ```python
    --8<-- "python/secuenciales/area_triangulo.py"
    ```
