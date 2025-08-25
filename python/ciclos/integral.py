from math import sin

N = int(input("Ingrese N: "))
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

dx = (b - a) / N
x = a
integral = 0
while x < b:
    integral += (sin(x) + x ** 2) * dx
    x += dx

print(integral)

x = a + dx
integral = 0
while x <= b:
    integral += (sin(x) + x ** 2) * dx
    x += dx

print(integral)