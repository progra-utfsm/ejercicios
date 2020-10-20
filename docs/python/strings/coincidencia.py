def coincide(s1, s2):
    # Encontrar la menor longitud
    lon = len(s1) # Suponer que el primer string es el mas corto
    if lon > len(s2): # Verificar si se cumple el supuesto
        lon = len(s2) # En el caso que el segundo string sea mas corto
    # Comparar letra a letra y guardar en una variable la coincidencia
    i = 0
    coincidencia = ''
    while i < lon: # Recorremos los indices
        if s1[i] == s2[i]: # Son iguales los caracteres?
            coincidencia += s1[i] # Concatenamos las letras similares
        i += 1
    return coincidencia
# Entrada
str1 = input("String 1: ")
str2 = input("String 2: ")
# Salida
print("Resultado:", coincide(str1, str2))