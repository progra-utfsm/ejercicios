# Costo llamadas internacionales

El costo de las llamadas telefónicas internacionales depende de la zona geográfica en la que se encuentra el país de destino y del número de minutos que se hablaron. Además, las llamadas que se inician en horario nocturno tienen un descuento del $20\%$.

|Código de zona|      Zona       |Precio por minuto|
|--------------|-----------------|-----------------|
|$12$          |América del Norte|$2$              |
|$15$          |América Central  |$2.2$            |
|$18$          |América del Sur  |$4.5$            |
|$19$          |Europa           |$3.5$            |
|$23$          |Asia             |$6$              |
|$25$          |África           |$6$              |
|$29$          |Oceanía          |$5$              |


Escriba un programa que lea como entrada la zona de una llamada, el horario (día o noche) y la cantidad de minutos, e indique el costo total de la llamada. Debe validarse que la zona, el horario y la cantidad de minutos sean válidos. De lo contrario, termina con error.

??? danger "Solución"
    ```python
    --8<-- "python/condicionales/llamadas.py"
    ```