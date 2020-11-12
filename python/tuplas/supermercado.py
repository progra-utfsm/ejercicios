def producto_mas_caro(productos):
    # Variables para guardar el producto mas caro
	max_precio = -1
	producto = ""
    # Recorremos la lista de tuplas y buscamos el producto de mayor precio
	for codigo, nombre, precio, unidades in productos:
		if precio >= max_precio:
			max_precio = precio
			producto = nombre
	return producto

def valor_total_bodega(productos):
	total = 0 # Acumulador para guardar el valor total de la bodega
    # Recorremos la estructura 
	for codigo, nombre, precio, unidades in productos:
		total += precio * unidades # multiplicamos la cantidad de unidades por el precio
	return total

def ingreso_total_por_ventas(itemes, productos):
	total = 0 # Variable para guardar el ingreso total
	for boleta, codigo, cantidad in itemes: # Recorremos la estructura itemes donde se mantiene cada transaccion
		for cod, nombre, precio, unidades in productos: # Recorremos los productos para obtener la info de cada producto
			if codigo == cod: # Si corresponde el codigo de producto
				total += cantidad * precio # Calculamos el ingreso asociado a dicho producto
	return total

def producto_con_mas_ingresos(itemes, productos):
    nombres = [] # Creamos una lista para guardar los nombres de cada producto - [nombre_producto_1, nombre_producto_2, ... ]
    ingreso = [] # Otra lista para guardar el ingreso de cada producto - [ingreso_por_producto_1, ingreso_por_producto_2, ...]
    for boleta, codigo, cantidad in itemes: # Recorremos la estructura itemes donde se mantiene cada transaccion
        for cod, nombre, precio, unidades in productos: # Recorremos los productos para obtener la info de cada producto
            if codigo == cod: # Si corresponde el codigo de producto
                # Guardaremos la informacion del nombre del producto y el ingreso respectivo (listas inicializadas)
                if nombre not in nombres: # Si todavia no agregamos el nombre del producto
                    nombres.append(nombre) # Se agrega
                    ingreso.append(cantidad * precio) # Y se agrega tambien el ingreso asociado al producto
                else: # Si el nombre del producto ya habia sido agregado
                    pos = nombres.index(nombre) # Obtenemos la posición 
                    ingreso[pos] += cantidad * precio # Actualizamos el ingreso mediante la posicion 
    # Buscamos ahora el mayor precio
    max_precio = max(ingreso) # Buscamos el maximo en la lista de ingresos
    max_pos = ingreso.index(max_precio) # Encontramos la posicion de ese maximo
    return nombres[max_pos] # Retornamos el nombre que se encuentra en la lista nombres utilizando la posicion respectiva

def cliente_que_mas_pago(itemes, productos, clientes, ventas):
    # Primero obtenemos las boletas con sus respectivos gastos
    boletas = [] # Id de la boleta -  [id_boleta_1, id_boleta_2, ... ]
    totales = [] # Totales de cada boleta - [total_boleta_1, total_boleta_2, ... ]
    for boleta, codigo, cantidad in itemes:
        for cod, nombre, precio, unidades in productos:
            if codigo == cod:
                if boleta not in boletas:
                    boletas.append(boleta)
                    totales.append(cantidad * precio)
                else:
                    pos = boletas.index(boleta)
                    totales[pos] += cantidad * precio
    # Ahora buscamos los clientes asociados a cada boleta para saber quien ha pagado mas
    nombres = [] # Para guardar los nombres de cada cliente - [nombre_cliente_1, nombre_cliente_2, ... ]
    pagos = [] # Para guardar el total pagado por cada cliente - [pago_cliente_1, pago_cliente_2, ... ]
    for boleta, fecha, rut in ventas:
        for rut_cliente, nombre_cliente in clientes:
            if rut == rut_cliente: # Filtramos por el rut respectivo
                pos_boleta = boletas.index(boleta) # Recuperamos el indice de la boleta 
                if nombre_cliente not in nombres: # Si todavia no existe el nombre del cliente
                    nombres.append(nombre_cliente) # Se agrega
                    pagos.append(totales[pos_boleta]) # Se agrega el pago asociado a esa boleta
                else: # Si ya existe el cliente
                    pos_nombre = nombres.index(nombre_cliente) # Lo buscamos
                    pagos[pos_nombre] += totales[pos_boleta] # Sumamos el gasto de otra boleta al que ya teniamos
    # Buscamos dentro de los pagos el mayor
    max_pago = max(pagos)
    max_pos = pagos.index(max_pago)
    return nombres[max_pos] # Retornamos el nombre asociado a esa posicion
                
def total_ventas_del_mes(year, month, itemes, productos, ventas):
    total = 0 # Acumulador del total
    for boleta, fecha, rut in ventas: # Recorremos las ventas
        año, mes, dia = fecha # Desempaquetamos la fecha
        if año == year and mes == month: # Filtramos por fecha
            for bol, prod, cant in itemes: # Recorremos los itemes para encontrar las boletas de la fecha
                if bol == boleta: # Filtramos por boleta
                    for producto in productos: # buscamos la informacion del producto
                        id_producto, _, precio, _ = producto 
                        if id_producto == prod: # Si el producto corresponde a la boleta analizada
                            total += cant * precio # Sumamos
    return total

def fecha_ultima_venta_producto(id_producto, itemes, ventas):
    fechas = [] # Lista para guardar las fechas donde se vendio el id_producto
    for numero_boleta, producto, _ in itemes: # Recorremos los detalles de ventas
        if id_producto == producto: # Si encontramos el producto
            for nb, fecha, _ in ventas: # Recorremos la informacion de ventas para recuperar la fecha
                if nb == numero_boleta: # Filtramos por el numero de boleta
                    fechas.append(fecha) # Agregamos la tupla con la fecha
    return max(fechas) # Retornamos la mayor tupla que corresponde a la ultima fecha c:


# Estructuras #
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

# Pruebas #
print(producto_mas_caro(productos))
print(valor_total_bodega(productos))
print(ingreso_total_por_ventas(itemes, productos))
print(producto_con_mas_ingresos(itemes, productos))
print(cliente_que_mas_pago(itemes, productos, clientes, ventas))
print(total_ventas_del_mes(2010, 10, itemes, productos, ventas))
print(fecha_ultima_venta_producto(47470, itemes, ventas))