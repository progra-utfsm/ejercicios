def distancia_origen(x, y):
    return (x ** 2 + y ** 2) ** 0.5

def mas_lejano(puntos):
    # Utilizamos el patron para buscar un maximo
    max_dist = -1 
    max_punto = []
    # Recorremos el arreglo
    for punto in puntos:
        # Calculamos la distancia al origen
        d = distancia_origen(punto[0], punto[1])
        if d > max_dist: # Guardamos la informacion del punto mas lejano 
            max_punto = punto
            max_dist = d
    return max_punto

def orden(puntos):
    # Creamos una lista donde guardaremos los puntos de manera "descendente"
    orden = [] 
    # Calcularemos el punto mas lejano y lo removeremos de la lista
    # Recorremos la lista de puntos mientras existan
    while len(puntos) > 0: 
        lejano = mas_lejano(puntos) # Obtenemos el punto mas lejano
        orden.append(lejano) # Lo agregamos a nuestra lista
        puntos.remove(lejano) # Lo removemos de los puntos
    orden.reverse() # Como agregamos los puntos en orden descendente, invertimos la lista
    return orden

# Puntos de ejemplo
puntos = [[0, 1], [-1, 1], [-10, 10], [2.3, 0.1], [1, 1.1], [2, 1], [0.4, 5]]
ordenado = orden(puntos) # Ordenamiento
print(ordenado) # Salida
