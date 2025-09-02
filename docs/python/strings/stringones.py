# Entrada 
abreviada = input("Palabra abreviada: ")
original = '' # Concatenaremos la palabra original
i = 0 # Para los indices del string
while i < len(abreviada): # Recorremos los indices del string
    n = int(abreviada[i]) # Obtenemos el numero de repeticiones
    l = abreviada[i+1] # Obtenemos la letra
    original += l * n  # Se concatena el texto con la repetición de cada letra
    i += 2 # Nos saltamos 2 indices, dada la estructura de los textos abreviados
print("Palabra original:", original)