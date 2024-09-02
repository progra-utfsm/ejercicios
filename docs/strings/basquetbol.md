# Básquetbol

En el básquetbol existen tres diferentes tipos de anotaciones:

- el tiro libre (`L`), que vale un punto,
- el doble (`D`), que vale dos puntos, y
- el triple (`T` ) que vale tres puntos.

Un partido de básquetbol está dividido en varios períodos.

Usted debe escribir un programa que reciba como entrada una única línea, que contenga todas las anotaciones realizadas por un equipo de básquetbol durante un partido. Las anotaciones de períodos distintos deben ir separadas por un espacio. Como salida, debe mostrar la cantidad de puntos obtenidos en cada período y los puntos totales, siguiendo el formato del ejemplo.

## Ejemplo

```
Anotaciones: DDTDLLDD DDLDT TDTLLD DDDDD
15 puntos en el periodo 1
10 puntos en el periodo 2
12 puntos en el periodo 3
10 puntos en el periodo 4
Total: 47 puntos
```

??? danger "Solución"
    ```python
    --8<-- "python/strings/basquetbol.py"
    ```