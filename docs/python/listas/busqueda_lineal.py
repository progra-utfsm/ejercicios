def busqueda_secuencial(lista, elemento):
    # Recorremos el arreglo utilizando indices
    for i in range(len(lista)):
        if elemento == lista[i]: # Si encontramos el elemento
            return i # Retornamos la posición
    return False # Si no lo encontramos, se retorna falso
# Pruebas
print(busqueda_secuencial([11,23,58,31,56,77,43,12,65,19], 31))
print(busqueda_secuencial([11,23,58,31,56,77,43,12,65,19], 13))