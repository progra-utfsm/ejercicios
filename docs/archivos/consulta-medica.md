# Consulta médica
Una consulta médica tiene un archivo pacientes.txt con los datos personales de sus pacientes. 
Cada línea del archivo tiene el rut, el nombre y la edad de un paciente, separados por un símbolo `:`. 

Así se ve el archivo:

???info "`pacientes.txt`"
    ```
    --8<-- "python/archivos/pacientes.txt"
    ```

Además, cada vez que alguien se atiende en la consulta, la visita es registrada en el archivo `atenciones.txt`, 
agregando una línea que tiene el rut del paciente, la fecha de la visita (en formato `dia-mes-año`) y el precio 
de la atención, también separados por `:`. El archivo se ve así:

???info "`atenciones.txt`"
    ```
    --8<-- "python/archivos/atenciones.txt"
    ```

Note que las fechas están ordenadas de menos a más reciente, ya que las nuevas líneas siempre se van agregando al final.

1. Escriba la función `costo_total_paciente(rut)` que entregue el costo total de las atenciones del paciente con el rut dado:
    ```
    >>> costo_total_paciente('8015253-1')
    297572
    >>> costo_total_paciente('14350739-4')
    0
    ```
2. Escriba la función `pacientes_dia(dia, mes, año)` que entregue una lista con los nombres de los pacientes que se atendieron el día señalado:
    ```
    >>> pacientes_dia(2, 6, 2010)
    ['Pablo Muñoz', 'Alfonso San Martín']
    >>> pacientes_dia(23, 6, 2010)
    []
    ```
3. Escriba la función `separar_pacientes()` que construya dos nuevos archivos:
    * `jovenes.txt`, con los datos de los pacientes menores de 30 años;
    * `mayores.txt`, con los datos de todos los pacientes mayores de 60 años.

    Por ejemplo, el archivo `jovenes.txt` debe verse así:
    ```
    15007265-4:Andrés Morales:26
    15690109-1:Francisco Ruiz:26
    13087677-3:Jorge Álvarez:28
    12028339-1:Jorge Argandoña:29
    14350739-4:Eduardo Bello:29
    ```
4. Escribir una función `ganancias_por_mes()` que construya un nuevo archivo llamado `ganancias.txt` que tenga el total de ganancias por cada mes en el siguiente formato:
    ``` 
    5-2010:933159
    6-2010:1120967
    7-2010:124903
    ```

??? danger "Solución"
    ```python
    --8<-- ";python/archivos/consulta_medica.py"
    ```