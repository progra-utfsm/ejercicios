# Programa que valida un triángulo y dice de qué tipo es
a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

if a + b > c and a + c > b and b + c > a: # Cumple desigualdad triangular
   
   # Se determina ahora el tipo de triángulo de acuerdo a sus lados:
   if a == b and b == c:
      print('El triángulo es equilátero')
   elif a == b or a == c or b == c:
      print('El triángulo es isósceles')
   else:
      print('El triángulo es escaleno')

   # Se determina ahora el tipo de triángulo de acuerdo a sus ángulos:
   # Primero se deja el lado mayor en hipotenusa y los restantes en a y b
   if a >= b and a >= c:
      temp = c
      c = a
      a = temp
   elif b >= a and b >= c:
      temp = c
      c = b
      b = temp
      
   # Ahora se determina el tipo
   if a ** 2 + b ** 2 == c ** 2:
      print('Además es rectángulo.')
   elif a ** 2 + b ** 2 < c ** 2:
      print('Además es obtusángulo.')
   else:
      print('Además es acutángulo.')
else:
   # No cumple la desigualdad triangular
   print('No es un triángulo válido.')
