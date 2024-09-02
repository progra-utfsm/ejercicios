# Asignaturas

Dado un `string` con el siguiente formato, pero del que desconocemos la cantidad de asignaturas: `"Progra=78;Mate=83;Física=68;Química=65"`. Escriba un programa que lea el string como entrada y calcule el promedio de calificaciones, indicando además la materia con mejor promedio. En caso de empate puede mostrar cualquiera de las que empatan.

## Ejemplo

```
Ingrese string: Progra=78;Mate=83;Física=68;Química=65
Promedio: 74
Mejor asignatura: Mate
```

??? danger "Solución 1"
    ```python
    --8<-- "python/strings/asignaturas.py"
    ```

??? danger "Solución 2"
    ```python
    --8<-- "python/strings/asignaturas_2.py"
    ```