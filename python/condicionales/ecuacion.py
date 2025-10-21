# Entrada de datos
a = float(input('a: '))
b = float(input('b: '))

if a != 0: # Si la ecuación tiene solución 
   x = -b / a
   print('x =', x)
else: # Si a == 0
   print('a debe ser distinto de cero')
