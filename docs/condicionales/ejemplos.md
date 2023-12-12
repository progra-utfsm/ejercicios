# Ejemplos varios

1. Escriba una condición lógica para la siguiente expresión: "Yo tengo horas de atención a estudiantes los lunes y los miércoles, siempre que no sea feriado, pero por superstición también atiendo todos los martes 13"

    ??? danger "Solución"
        ```python
        a = ( (dia == 'Lunes' or dia == 'Miércoles') and not feriado ) or (dia == 'Martes' and fecha == 13)
        ```

2. Dado el siguiente programa:
    ```python
    n = int(input())
    if n < 0:
        n = abs(n)
    print(n)
    ```
    ¿Cuántas veces en total se ejecuta la instrucción `n = abs(n)` en $10$ ejecuciones distintas con las siguientes entradas: `5 -2 0 0 -3 -1 7 0 2 -2`? En el mismo escenario, ¿cuántas veces se ejecuta la instrucción `print(n)`?

    ??? danger "Solución"
        $4$ y $10$

3. El siguiente programa que determina el nivel de estudios de una persona a partir de su edad:
    ```python
    if edad < 6:
        print('Preescolar')
    elif edad < 18:
        print('Escolar')
    elif edad < 25:
        print('Universitario')
    else:
        print('Postgrado')
    ```
    ¿Qué condición debe cumplirse para que imprima Escolar? ¿Y para que llegue al else?

    ??? danger "Solución"
        - Entre $6$ y $17$
        - Mayor o igual a $25$.

    ¿Es equivalente este código?

    ```python
    if edad < 6:
        print('Preescolar')
    if edad < 18:
        print('Escolar')
    if edad < 25:
        print('Universitario')
    else:
        print('Postgrado')
    ```

    ??? danger "Solución"
        **No**, por ejemplo ¿qué ocurre con $5$?
        
4. Haga el ruteo del siguiente programa para las entradas que se indican.
    ```python
    --8<-- "python/condicionales/ruteo_bisiesto.py"
    ```
    Entradas:

    1. `29 2 2020`
    2. `31 6 2020`
    3. `31 7 2020`