# Conductores

Considerando la siguiente estructura de datos:

```python
conductores = {
    #username: [nombre, puntaje, [marca, modelo]]
    'azambrano': ['Andres Zambrano', 5.6, ['Hyundai', 'Elantra']],
    'jojeda': ['Juan Ojeda', 1.1, ['Hyundai', 'Accent']],
    #...
}
``` 

a) Desarrolle la función `agrega_conductor(conductores, nuevo_conductor)` donde
`nuevo_conductor` corresponde a una lista con los siguientes datos `[username, nombre_completo, puntaje, [marca, modelo]]`. Por ejemplo;
```python
>>> agrega_conductor(conductores,['fsoto', 'Fabiola Soto', 4.4, ['Peugeot', '308']])
True
```
La función debe modificar el diccionario y retornar `True`. Si el `username` del conductor a
agregar ya existe, no modifique el diccionario y sólo retorne `False`.

b) Desarrolle la función `elimina_conductor(condutores, username)` que elimine el conductor
con el `username` desde la estructura conductores.
```python
>>> elimina_conductor(conductores, 'jojeda')
True
>>> elimina_conductor(conductores, 'pmunoz')
False
```
c) Desarrolle la función `ranking(conductores)` que recibe el diccionario conductores y entrega
una lista de listas con los `usernames` y puntajes, ordenados de mayor a menor puntaje.
Por ejemplo;
```python
>>> ranking(conductores)
[['Andres Zambrano', 5.6], ['Fabiola Soto', 4.4]]
```

???danger "Solución"
    ```python
    --8<-- "python/diccionarios/conductores.py"
    ```