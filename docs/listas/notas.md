# Notas

El profesor de una asignatura de la USM registra las notas de sus alumnos en una lista como la siguiente:

```python
alumnos = [
    ['Alberto Gonzalez', 40, 30, 70], 
    ['Francisca Almonacid', 100, 40],
    ['Pedro Reyes', 30, 50],
    ['Juan Campos', 30, 60, 30, 70],
    ['Andrea Zamora', 30],
    #...
]
```

Los datos que se almacenan, para cada alumno, son el nombre y una cantidad variable de notas. Como se ve en el ejemplo, la cantidad de notas puede variar de un alumno a otro.

Se le pide que escriba las siguientes funciones:

1. La función `calcular_promedio(alumnos)` que recibe la lista alumnos con la estructura que se indicó, y retorna una nueva lista que contiene el nombre y el promedio de cada alumno.

## Ejemplo:

```python
>>> calcular_promedio(alumnos)
[ ['Alberto Gonzalez', 47], ['Francisca Almonacid', 70],
    ['Pedro Reyes', 40], ['Juan Campos', 48], ['Andrea Zamora', 30]
]
```

2. La funcion `mejor_promedio(alumnos)` que entrega el nombre del alumno con mejor promedio. Si hay varios alumnos empatados con el mejor promedio, la función retorna alguno de ellos, sin importar cuál.

## Ejemplo:

```python
>>> mejor_promedio(alumnos)
'Francisca Almonacid'
```

??? danger "Solución"
    ```python
    --8<-- "python/listas/notas.py"
    ```