# Delitos

Considerando las siguientes estructuras:
```python
calles = [
    # (id_calle1, nombre_calle1), …
    (883345, 'La Montana'), (321333, 'Miraflores'), (5843, 'Avellaneda'),
    (2283904, 'Del Valle'), (9430, 'Los Maitenes'), (2239102, 'Rio Tolten'),
    (9432, 'Teniente Bello')
]
niveles_peligrosidad = {
    #nivel: [id_calle1, id_calle2, id_calle3, …]
    2: [883345, 2283904, 5843],
    1: [9430, 2239102,9432], 
    # ...
}
delitos = [
    { 'id_calle': 883345, 'fecha': '2015-03-23'},
    { 'id_calle': 9432, 'fecha': '2015-02-12'},
    { 'id_calle': 5843, 'fecha': '2015-03-21'}, 
    # ...
]
```
a) Desarrolle la función `agregar_delito(delito, delitos)` que recibe la tupla `delito`
con los datos a agregar, y la lista de delitos. Si la función logra agregar el delito, debe
retornar `True`, en caso de error debe retornar `False`. Para agregar un delito correctamente la calle
debe existir y tener asociado un nivel de peligrosidad.
```python
>>> agregar_delito((9430, (2016, 1, 1)), delitos)
True
>>> agregar_delito((322, (2016, 3, 23)), delitos)
False
```
b) Desarrolle la función `mes_mas_peligroso(anio, delitos)` que recibe la lista de delitos
y el año. Esta función debe entregar el nombre del mes del año en el que ocurren más delitos.
```python
>>> mes_mas_peligroso(2015, delitos)
'Marzo'
```

???danger "Solución"
    <!--
    ```python
    --8<-- "python/diccionarios/viajes.py"
    ```
    -->