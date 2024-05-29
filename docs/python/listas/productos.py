def actualizar_unidades_a(categoria, marca, unidades, productos):
    for i in range(len(productos)):
        if categoria == productos[i][0] and marca == productos[i][1]:
            productos[i][2] = unidades
    return productos

def actualizar_unidades_b(categoria, marca, unidades, productos):
    agregar = True
    for i in range(len(productos)):
        if categoria == productos[i][0] and marca == productos[i][1]:
            productos[i][2] = unidades
            agregar = False
    if agregar:
        print("El producto: " + categoria + " (" + marca + ") no es encuentra en los registros.")
        pasillo = int(input("Indique pasillo: "))
        nuevo_producto = [categoria, marca, unidades, pasillo]
        productos.append(nuevo_producto)
    tmp = []
    for producto in productos:
        tmp.append([producto[-1], producto])
    tmp.sort()
    productos = []
    for producto in tmp:
        productos.append(producto[1])
    return productos

def borrar_productos(lista_productos, productos):
    eliminar = [] # Guardar el índice de los productos a eliminar
    for i in range(len(productos)):
        for p in lista_productos:
            cat = p[0]
            mar = p[1]
            if productos[i][0] == cat and productos[i][1] == mar:
                eliminar.append(i)
    eliminar.sort()
    eliminar.reverse() # Debemos eliminar de atrás hacia adelante para no alterar los índices
    for e in eliminar:
        del productos[e]
    return productos    

def borrar_productos(lista_productos, productos):
    borrar = [] # Guardar los productos a borrar
    for p in lista_productos:
        for producto in productos:
            if p[0] == producto[0] and p[1] == producto[1]:
                if producto not in borrar:
                    borrar.append(producto)
    for b in borrar:
        productos.remove(b)
    return productos
                
productos = [
    ['fideos', 'carozzi', 30, 1],
    ['arroz', 'tucapel', 23, 2]
    # ...
]

print(productos)
productos = actualizar_unidades_a('fideos', 'carozzi', 15, productos)
print(productos)
lista_productos = [['azúcar', 'ianza'], ['fideos', 'carozzi']]
productos = borrar_productos(lista_productos, productos)
print(productos)
