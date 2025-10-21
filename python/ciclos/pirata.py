from random import randint
from math import sqrt
# Posicion del tesoro
a = randint(0, 100)
b = randint(0, 100)
encontrado = False # Variable 
while not encontrado:
    # Intento de adivinar
    x = int(input('Ingrese x: '))
    y = int(input('Ingrese y: '))
    # Verificar
    if x == a and y == b:
        encontrado = True
    else:
        # Calculo de distancia
        d = round(sqrt((a - x) ** 2 + (b - y) ** 2), 2)
        print('Tesoro a', d)
# Luego de terminar el ciclo, el tesoro fue encontrado
print('Tesoro encontrado')
