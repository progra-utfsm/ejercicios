def mayor_movilidad(transitos):
    # Conteo de patentes #
    conteo = {} # Diccionario para realizar conteo
    for transito in transitos: # Recorrido de la estructura
        patente = transito[0] # Patente
        if patente not in conteo: # Si la patente no existe 
            conteo[patente] = 0 # Creamos el contador
        conteo[patente] += 1 # Sumamos uno cada vez que encontremos la patente
    # Lista temporal para ordenar segun el conteo #
    lista = [] # Estructura: [[conteo_1, patente_1], [conteo_2, patente_2], ...]
    for patente in conteo: # Recorremos el diccionario
        tmp = [conteo[patente], patente] # Dejamos el conteo primero para ordenar con sort
        lista.append(tmp) # Agregamos la lista temporal
    lista.sort() # Ordenamos ascendentemente
    lista.reverse() # Ordenamos descendentemente
    # Lista de salida segun el formato solicitado #
    salida = []
    for conteo, patente in lista[:3]: # Recorremos solo los primeros 3 que necesitamos
        salida.append([patente, conteo]) # Volvemos al orden solicitado
    return salida


def reportar(transitos):
    reporte = {} # Diccionario a retornar
    for transito in transitos: # Recorrido de la estructura
        patente = transito[0]
        portico = transito[1]
        if portico not in reporte: # Si no existe el portico en el diccionario
            reporte[portico] = [] # Se crea una lista vacia
        if patente not in reporte[portico]: # Si la patente no existe en la lista
            reporte[portico].append(patente) # Se agrega
        reporte[portico].sort() # Ordenamos la lista de patentes en orden alfabetico
    return reporte # Retornar diccionario

# Estructura de prueba #
transitos = [
    ['BBJJ77',2], 
    ['CCHH19',3], 
    ['AAFF37',3], 
    ['BBJJ77',1], 
    ['AAFF37',1], 
    ['DDKK33',3], 
    ['AAFF37',1], 
    ['AAFF37',2]
]

# Pruebas #
print(mayor_movilidad(transitos))
print(reportar(transitos))