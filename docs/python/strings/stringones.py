def original(abreviada):
    out = '' # Concatenaremos la palabra original
    i = 0 # Para los indices del string
    while i < len(abreviada): # Recorremos los indices del string
        n = int(abreviada[i]) # Obtenemos el numero de repeticiones
        l = abreviada[i+1] # Obtenemos la letra
        out += l * n  # Se concatena el texto con la repetición de cada letra
        i += 2 # Nos saltamos 2 indices, dada la estructura de los textos abreviados
    return out

# Entrada y salida
abr = input("Ingrese palabra abreviada: ")
print("Original:", original(abr))