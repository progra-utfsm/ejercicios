# Pago de horas extra

Dada la cantidad de horas trabajadas en una semana por una persona, se debe calcular el monto que se le debe pagar por concepto de horas extra, es decir, por las horas trabajadas por sobre las $44$ obligatorias.

Se debe leer también la categoría del empleado (un entero entre $1$ y $5$), pues dependiendo de la categoría es el monto a pagar por cada hora extra. Los de categoría $1$ reciben $\$ 5.000$ por hora extra, los de categoría $2$ reciben $\$8.000$ y los de categoría $3$ reciben $\$10.000$. Los de categoría $4$ y $5$ no tienen derecho al pago por sus horas extra.

El máximo número de horas extra que se pueden pagar en una semana es $10$. Si se trabajan más, no se recibe pago alguno.

??? danger "Solución"
    ```python
    --8<-- "python/condicionales/horas_extra.py"
    ```