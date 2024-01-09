def producto_interno(u, v):
    n = len(u) # u y v tienen el mismo tamaño
    productos = [] # Lista para guardar los productos
    for i in range(n): # Recorremos los elementos de u y v
        productos.append(u[i] * v[i]) # Guardamos el producto
    return sum(productos) # Sumamos los productos