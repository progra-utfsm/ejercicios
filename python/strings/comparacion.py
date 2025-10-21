# Entradas
s1 = input("String 1: ")
s2 = input("String 2: ")
tol = int(input("Tolerancia: "))
# Algoritmo
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
# Salida
if dif <= tol:
    print("Iguales con tolerancia =", tol)
else:
    print("Distintos con tolerancia =", tol)