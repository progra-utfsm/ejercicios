from math import sin, pi

# Entradas
a = float(input("Ingrese el valor del lado a (metros): "))
b = float(input("Ingrese el valor del lado b (metros): "))
theta = float(input("Ingrese el valor del ángulo theta (grados): "))

# Cálculos
angulo = theta * pi / 180
area = round(a * b * sin(angulo) / 2, 2)

# Salidas
print("El área del triángulo es:", area, "metros cuadrados")
