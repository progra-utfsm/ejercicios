# Crédito Hipotecario

La cuota mensual $m$ que se debe pagar en un crédito hipotecario por un capital inicial $h$ a un plazo de $n$ años, utilizando un interés compuesto de $i\%$ anual está dada por:

\begin{equation}
    m = \dfrac{h\,r}{1-(1+r)^{-12n}},
\end{equation}

donde

\begin{equation}
    r = \dfrac{i}{100\cdot 12}
\end{equation}

1. Escriba la función `cuota_mensual` que calcula la cuota mensual para un capital inicial, un plazo y una tasa de interés dados, redondeado a $2$ decimales. Ej: para $\$50.000.000$, $15$ años y $4,75\%$, debe entregar $\$388.915,96$ (todo como números, sin $\$$ ni $\%$).
2. Escriba la función `monto_total` que calcula el monto total que se pagará en el total en el crédito. Para el ejemplo sería: $\$70.004.872,8$
3. Escriba la función `intereses_pagados` que calcula el monto total por intereses que se pagará en todo el crédito. Para el ejemplo sería: $\$20.004.872,8$
4. Escriba la función `porcentaje_intereses` que calcula el porcentaje del capital inicial que se pagará en intereses en todo el crédito. Para el ejemplo sería: $40,01\%$
5. Escriba un programa que para un capital inicial y una tasa de interés dados, muestre los valores de cuota mensual, monto total a pagar y porcentaje que se pagará en intereses, para un rango de plazos (años). Por ejemplo de $10$ a $25$:
    ```
    10 524238.72 62908646.4 25.82 
    11 487057.28 64291560.96 28.58 
    12 456199.58 65692739.52 31.39 
    ...
    25 285058.68 85517604.0 71.04
    ```

??? danger "Solución"
    ```python
    --8<-- "python/funciones/hipoteca.py"
    ```