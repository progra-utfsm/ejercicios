# PyCornerShop

La empresa *PyCornerShop* dispone de una aplicación que permite a sus usuarios conseguir productos del supermercado desde la comodidad del hogar usando sus teléfonos móviles. La información de los repartidores y usuarios se encuentra almacenada en dos listas llamadas `repartidores` y `usuarios`, respectivamente.

La lista `usuarios` contiene listas de 2 elementos: Código del usuario y ubicación del domicilio. Esta última corresponde a una lista que representa las coordenadas x, y. La lista `repartidores` contiene listas de 4 elementos: El nombre del repartidor, su ubicación actual (lista con coordenadas), disponibilidad (valor booleano) y lista de visitas a usuarios. Esta lista contiene listas con el código del usuario y la cantidad de veces que ha sido visitado por el repartidor. Si un repartidor nunca ha visitado a un usuario, no aparecerá en la lista ni una tupla ni un código de ese usuario.

Para que *PyCornerShop* pueda funcionar de manera eficiente, le solicita a Ud. que implemente una función llamada `buscar_repartidor(usuarios, repartidores, codigo)` que reciba como parámetros las listas antes mencionadas y un código de usuario. La función debe retornar una lista de repartidores disponibles más cercanos, ordenados de manera descendente según el número de visitas que haya realizado al usuario. Un repartidor se considera cercano si está ubicado a menos de 4 km del usuario, y para esto considere que las listas de ubicación tienen valores enteros con unidades en km. Finalmente, si no hay repartidores cercanos, la función debe retornar una lista vacía.


## Ejemplos

```python
repartidores = [
    ['rayo macuin', [10, 2], True, [[1221, 5], [441, 8], [587, 2]]],
    ['reparti dhor', [9, 3], True, [[1221, 2], [441, 5], [587, 3]]],
    ['eliseo al-azar', [5, 5], False, [[1221, 8], [441, 2]]]
]
usuarios = [[1221, [5, 2]], [441, [8, 2]], [587, [10, 1]]]

>>> buscar_repartidor(usuarios, repartidores, 1221)
[] # No hay repartidos que cumplan lo solicitado
```

```python
repartidores = [
    ['rayo macuin', [6, 3], True, [[1221, 5], [441, 8], [587, 2]]],
    ['reparti dhor', [7, 2], True, [[1221, 2], [441, 5], [587, 3]]],
    ['eliseo al-azar', [5, 4], True, [[1221, 8], [441, 2]]]
]
usuarios = [[1221, [5, 2]], [441, [8, 2]], [587, [10, 1]]]

>>> buscar_repartidor(usuarios, repartidores, 1221)
['eliseo al-azar', 'rayo macuin', 'reparti dhor']
```

??? danger "Solución"
    ```python
    --8<-- "python/listas/pycornershop.py"
    ```