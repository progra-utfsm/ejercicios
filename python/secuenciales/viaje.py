from math import sqrt

# Entrada de coordenadas
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))
x3 = float(input('x3: '))
y3 = float(input('y3: '))

# Cálculo de distancias
d1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
d2 = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
d3 = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

# Salida de distancia total
print(d1 + d2 + d3)