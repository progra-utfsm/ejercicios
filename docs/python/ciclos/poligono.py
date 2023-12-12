from math import sqrt

n = int(input('lados: '))
print('Punto 1')
x1 = float(input('x: '))
y1 = float(input('y: '))
x0 = x1
y0 = y1
perimetro = 0
i = 2
while i <= n:
   print('Punto', i)
   x2 = float(input('x: '))
   y2 = float(input('y: '))
   d = sqrt((x2-x1)**2 + (y2-y1)**2)
   perimetro += d
   x1 = x2
   y1 = y2
   i += 1
d = sqrt((x1-x0)**2 + (y1-y0)**2)
perimetro += d
print('Perímetro:', perimetro)