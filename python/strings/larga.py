def palabra_mas_larga(texto):
    larga = "" # Variable donde guardaremos la palabra mas larga
    i = 0 # Indice para recorrer el texto
    j = 0 # Indice para guardar las posiciones de los espacios
    # Recorremos el texto utilizando el indice i
    while i < len(texto):
        if texto[i] == " ": # Si encontramos un espacio
            # Utilizamos el substring que contiene la palabra a verificar
            if len(texto[j:i]) > len(larga): # Comparamos si la longitud es la mayor
                larga = texto[j:i] # La guardamos
            j = i + 1 # j guardara la posicion del ultimo espacio + 1 (para no contar el mismo espacio)
        i += 1
    # El ciclo anterior solo analizara las palabras cuando encuentre un espacio en el texto
    # Para verificar la ultima palabra utilizamos el siguiente condicional
    # j contiene la posicion del ultimo espacio + 1, y obtenemos hasta el final del substring
    if len(texto[j:]) > len(larga): 
        larga = texto[j:]
    return larga
# Entrada de texto
texto = input("Ingrese texto: ")
# Salida de respuesta
print("La palabra mas larga es:", palabra_mas_larga(texto))