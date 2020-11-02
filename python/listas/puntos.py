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
    
# Puntos de ejemplo
puntos = [[0, 1], [1, 1.1], [2, 1], [0.4, 5]]
punto = mas_lejano(puntos)
print("Punto mas lejano:", punto)


