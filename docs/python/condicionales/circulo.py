from math import sqrt

# Entrada de datos
print('Círculo:')
xc = float(input('x: '))
yc = float(input('y: '))
r = float(input('radio: '))
print('Punto:')
xp = float(input('x: '))
yp = float(input('y: '))

# Cálculo distancia
d = sqrt((xc - xp) ** 2 + (yc - yp) ** 2)

# Posición del punto
if d < r:
   print('El punto está dentro del círculo')
elif d > r:
   print('El punto está fuera del círculo')
else:
   print('El punto está justo sobre el perímetro del círculo')
