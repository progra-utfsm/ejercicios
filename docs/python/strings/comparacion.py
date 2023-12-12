def comparacion(s1, s2, tol):
    dif = 0 # Contador para los caracteres distintos
    # Obtencion de menor longitud
    lon = len(s1)
    if len(s2) < lon:
        lon = len(s2)
    # Recorrer cadenas
    i = 0
    while i < lon:
        if s1[i] != s2[i]: # Se cuentan los caracteres distintos
            dif +=1  
        i += 1 
    # Retorna True si la diferencia es menor o igual a la tolerancia
    # Caso contrario False
    return dif <= tol
# Entradas
str1 = input("String 1: ")
str2 = input("String 2: ")
tolerancia = int(input("Tolerancia: "))
# Salida
if comparacion(str1, str2, tolerancia):
    print("Iguales con tolerancia =", tolerancia)
else:
    print("Distintos con tolerancia =", tolerancia)