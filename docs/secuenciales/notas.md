# ¿Qué nota necesito?

Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
El promedio del ramo se calcula con la siguiente formula.

\begin{equation}
    \begin{split}
        N_C &= \dfrac{(C_1 + C_2 + C _3)}{3} \\[.5em]
        N_F &= 0.7\, N_C + 0.3\,N_L
    \end{split}
    \nonumber
\end{equation}

Donde $N_C$ es el promedio de certámenes, $N_L$ el promedio de laboratorio y $N_F$ la nota final.

Escriba un programa que pregunte al usuario las notas de los dos primeros certámenes y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final $60$.

## Ejemplo

```
Ingrese nota certamen 1: 45
Ingrese nota certamen 2: 55
Ingrese nota laboratorio: 65
Necesita nota 72 en el certamen 3
```

??? danger "Solución"
    ```python
    --8<-- "python/secuenciales/notas.py"
    ```
