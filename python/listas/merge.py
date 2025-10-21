def merge(lista1, lista2):
    # Nueva lista para guardar elementos
    nueva = list() 
    # Vamos extraer los primeros elementos de cada lista y compararlos mientras se pueda
    while len(lista1) > 0 and len(lista2) > 0:
        # Si el primer elemento de la primera lista es menor o igual que el de la segunda
        if lista1[0] <= lista2[0]:
            # Lo agregamos a nuesta nueva lista
            nueva.append(lista1[0]) 
            # Removemos el primer elemento de la primera lista
            lista1 = lista1[1:]
        else: # Si el primer elemento de la segunda lista es menor
            # Se agrega a la nueva lista
            nueva.append(lista2[0]) 
            # Removemos el primer elemento de la segunda lista
            lista2 = lista2[1:]
    # Notar que en algun momento una de las dos listas quedara vacia antes que la otra
    # Con los ciclos que siguen vamos a agregar los elementos sobrantes a nuesta nueva lista
    # Solo uno de los siguientes dos ciclos se ejecutara
    for v1 in lista1:
        nueva.append(v1)
    for v2 in lista2:
        nueva.append(v2)
    return nueva
# Prueba
l1 = [1, 1, 2, 3, 5, 6, 10, 12]
l2 = [0, 2, 5, 5, 7, 8]
print(merge(l1, l2))