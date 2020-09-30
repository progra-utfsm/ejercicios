# Numero de valores
n = int(input("Cuantos valores ingresara? "))
i = 1

# Variables para buscar menor y mayor
mayor = float("-inf") # Comenzar con un numero muy pequeño
menor = float("inf") # Comenzar con un numero muy grande

# Ingresar valores
while i <= n:
    v = float(input("Valor " + str(i) + ": "))
    if v > mayor:
        mayor = v
    if v < menor:
        menor = v
    i += 1

# Calcular rango y dejar con dos decimales
rango = round(mayor - menor, 2)
print("El rango es", rango)