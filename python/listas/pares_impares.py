from random import choice, randint
# Creacion de lista 
lista = list(range(randint(20, 50)))
# Estructuras para guardar los valores
pares = []
impares = []
# Se recorre la lista
for valor in lista:
    # Verificamos si el valor es para o impar y lo guardamos en la lista correspondiente
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
# Mostrar los valores
print("Pares:", pares)
print("Impares:", impares)