def busqueda_binaria(lista, elemento):
    i = 0 # Indice izquierdo de la lista
    d = len(lista) - 1 # Indice derecho de la lista
    while i <= d: # Buscamos mientras no se crucen los indices
        m = (d + i) // 2 # Punto medio
        if lista[m] == elemento: # Si encuentra el elemento
            return True # Retorna verdadero
        elif lista[m] > elemento: # Si el valor del elemento es menor 
            # Nos quedamos con la parte izquierda del arreglo, es decir, el indice derecho es el punto medio - 1
            d = m - 1  
        elif lista[m] < elemento: # Si el valor del elemento es mayor
            # Nos quedamos con la parte derecha del arreglo, es decir, el indice izquierdo es el punto medio + 1
            i = m + 1
    return False # No encontramos el elemento
# Pruebas
print(busqueda_binaria([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(busqueda_binaria([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))