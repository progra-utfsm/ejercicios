def veces(chico, grande):
    cont = 0 # Contador para las repeticiones
    i = 0 # Indice para recorrer el string
    # Recorremos el string grande, utilizando indices, sin contar la ultima parte (tamaño del string chico)
    # La idea es comparar el string pequeño con el substring del grande entre los indices [i:i+len(chico)]
    while i <= (len(grande) - len(chico)): 
        # Comparamos el string chico con el substring del grande
        if chico == grande[i: i+len(chico)]: 
            cont += 1 # Contador de repeticiones
        i += 1 
    return cont
# Entrada de strings
grande = input("Ingrese string grande: ")
chico = input("Ingrese string chico: ")
# Salida
print("Las palabra", chico, "aparece", veces(chico, grande), "veces en", grande)
