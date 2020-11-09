"""
	Ejercicio Supermercado
	http://progra.usm.cl/apunte/ejercicios/2/supermercado.html
"""

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

clientes = [
	('11652624-7', 'Perico Los Palotes'),
	( '8830268-0', 'Leonardo Farkas'),
	( '7547896-8', 'Fulanita de Tal'),
]

ventas = [
	(1, (2010,  9, 12),  '8830268-0'),
	(2, (2010,  9, 19), '11652624-7'),
	(3, (2010,  9, 30),  '7547896-8'),
	(4, (2010, 10,  1),  '8830268-0'),
	(5, (2010, 10, 13),  '7547896-8'),
	(6, (2010, 11, 11), '11652624-7'),
]

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

def producto_mas_caro(productos):
	max_precio = -1
	producto = ""
	for codigo, nombre, precio, unidades in productos:
		if precio >= max_precio:
			max_precio = precio
			producto = nombre
	return producto

def valor_total_bodega(productos):
	total = 0
	for codigo, nombre, precio, unidades in productos:
		total += precio * unidades
	return total

def ingreso_total_por_ventas(itemes, productos):
	total = 0
	for boleta, codigo, cantidad in itemes:
		for cod, nombre, precio, unidades in productos:
			if codigo == cod:
				total += cantidad * precio
	return total

print(producto_mas_caro(productos))
print(valor_total_bodega(productos))
print(ingreso_total_por_ventas(itemes, productos))