# Salario

El salario imponible de una persona se determina a partir del monto que percibe por las horas trabajadas, descontando el aporte previsional para su pensión y la cotización de salud. Al monto resultante se le aplica la siguiente tabla para calcular el Impuesto Único de Segunda Categoría que debe pagar:

| Hasta        |Tasa    |Descontar       |
|--------------|--------|----------------|
|$\$680.022$   |Exento  |                |
|$\$1.511.160$ |$4\%$   |$\$27.200,88$   |
|$\$2.518.600$ |$8\%$   |$\$87.647,28$   |
|$\$3.526.040$ |$13.5\%$|$\$226.170,28$  |
|$\$4.533.480$ |$23\%$  |$\$561.144,08$  |
|$\$6.044.640$ |$30.4\%$|$\$896.621,60$  |
|$\$15.615.320$|$35\%$  |$\$1.174.675,04$|
|y más         |$40\%$  |$\$1.955.441,04$|

El descuento de la Isapre corresponde a un $7\%$ del salario base, mientras que el descuento que hace la AFP corresponde a un $10\%$ para el ahorro y un $1,27\%$ para comisión.

El salario base se calcula a partir de las horas trabajadas en el mes. Cada empleado tiene un monto por hora que recibe. Las horas extra (por sobre $44$) se le pagan a $1,5$ veces el monto por hora regular. No se pagan más de $40$ horas extra mensuales.

Aplique descomposición de problemas para implementar un programa que calcule el salario que recibirá un empleado al término de un mes, indicando el detalle de lo ganado y lo descontado.

## Ejemplo
```
Monto por hora: $20000
Horas trabajadas: 45
Base: $ 910000
Impuestos: $ 9199
Sueldo: $ 900801
```

??? danger "Solución"
    ```python
    --8<-- "python/funciones/salario.py"
    ```

