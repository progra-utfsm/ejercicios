# Entrada de datos
x1 = float(input("Ingrese el valor de x1: "))
y1 = float(input("Ingrese el valor de y1: "))
x2 = float(input("Ingrese el valor de x2: "))
y2 = float(input("Ingrese el valor de y2: "))
x3 = float(input("Ingrese el valor de x3: "))
y3 = float(input("Ingrese el valor de y3: "))

# Cálculos
lado1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
lado2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
lado3 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
perimetro = lado1 + lado2 + lado3

# Salidas
print("El perímetro del triángulo es:", perimetro)