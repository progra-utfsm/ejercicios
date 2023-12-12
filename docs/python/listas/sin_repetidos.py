def sin_repetidos(lista):
    nueva = [] # Lista a retornar
    for val in lista: # Recorremos la lista original
        if val not in nueva: # Si no encontramos el valor en la que retornaremos
            nueva.append(val) # Agregamos el elemento
    return nueva 

lista = [1, 2, 2, 1, 4, 6, 2, 3, 4, 4, 1]
print("Lista original:", lista)
print("Sin repetidos:", sin_repetidos(lista))

