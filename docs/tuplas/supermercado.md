# Supermercado

Un supermercado utiliza tablas de datos para llevar la información de su inventario.

En un programa, cada tabla de datos es una lista de tuplas.

La lista `productos` tiene el código, el nombre, el precio y la cantidad de unidades del producto en bodega:

```python
productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]
```

La lista `clientes` tiene el rut y el nombre de los clientes del supermercado:

```python
clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ( '8830268-0', 'Leonardo Farkas'),
    ( '7547896-8', 'Fulanita de Tal'),
]
```

La lista `ventas` contiene las ventas realizadas, representadas por el número de boleta, la fecha de la venta y el rut del cliente:

```python
ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]
```

El detalle de cada venta se encuentra en la lista `itemes`. Cada ítem tiene asociado un número de boleta, un código de producto y una cantidad:

```python
itemes = [
    (1, 89148,  3),
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6),
    (3, 30877,  1),
    (4, 89148,  1),
    (4, 75466,  2),
    (5, 89148,  2),
    (5, 47470, 10),
    (6, 41419,  2),
]
```

Por ejemplo, en la venta con boleta número $2$, fueron vendidas $4$ paltas, $2$ bebidas y $6$ yogures.

Escriba las siguienes funciones:

```
>>> producto_mas_caro(productos)
'Vuvuzela'
>>> valor_total_bodega(productos)
1900570
>>> ingreso_total_por_ventas(itemes, productos)
13944
>>> producto_con_mas_ingresos(itemes, productos)
'Arroz'
>>> cliente_que_mas_pago(itemes, productos, clientes, ventas)
'Fulanita de Tal'
>>> total_ventas_del_mes(2010, 10, itemes, productos, ventas)
4160
>>> fecha_ultima_venta_producto(47470, itemes, ventas)
(2010, 10, 13)
```

??? danger "Solución"
    ```python
    --8<-- "python/tuplas/supermercado.py"
    ```