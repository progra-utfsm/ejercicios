# Productos

El personal encargado de reponer productos en un supermercado actualiza una lista de productos de acuerdo a lo que va encontrando en su recorrido por los pasillos. Se tiene una lista de productos como la siguiente:
```python
productos = [ ['fideos', 'carozzi', 30, 1], ['arroz', 'tucapel', 23, 2], ...]
```
Los productos son almacenados de acuerdo a su categoría, marca, número de unidades y pasillo en el que se encuentra.

## Ejercicios

a. Cree la función `actualizar_unidades_a(categoría, marca, unidades,
productos)` que recibe una categoría, una marca, el nuevo número de unidades de ese producto y la lista productos. El programa debe retornar la lista productos con el nuevo número de unidades. Considere que los productos y marcas a actualizar ya están incluidos en la lista productos.

```python
>>> productos = actualizar_unidades_a('fideos', 'carozzi', 15, productos)
>>> print(productos)
[['fideos', 'carozzi', 15, 1], ['arroz', 'tucapel', 23, 2]]
```
b. Modifique el programa anterior para que cuando se quiera actualizar un producto no incluido en la lista productos original, se cree un nuevo registro. Cuando se quiera actualizar un producto que no se encuentra en productos, el programa debe solicitar al usuario el ingreso del pasillo en el cual el producto se encuentra. La función debe retornar la lista productos ordenada de menor a mayor según el número de pasillo.
```python
>>> productos = actualizar_unidades_b('azúcar', 'ianza', 12, productos)
El producto: azúcar (ianza) no es encuentra en los registros.
>>> Indique número de pasillo: 1
>>> print(productos)
[['azúcar', 'ianza', 12, 1], ['fideos', 'carozzi', 15, 1], ['arroz',
'tucapel', 23, 2]]
```

c. Cree la función `borrar_productos(lista_productos, productos)` que permita eliminar los productos contenidos en lista_productos de la lista productos.
Considere el siguiente ejemplo:
```python
>>> lista_productos = [['azúcar', 'ianza'], ['fideos', 'carozzi']]
>>> productos = borrar_productos(lista_productos, productos)
>>> print(productos)
[['arroz', 'tucapel', 23, 2]]
```

??? danger "Solución"
    ```python
    --8<-- "python/listas/productos.py"
    ```