Nx = int(input("Ingrese Nx: "))
Ny = int(input("Ingrese Ny: "))
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))

dx = (b - a) / Nx
dy = (d - c) / Ny
x = a
integral = 0
while x < b:
    y = c
    while y < d:
        integral += -(x ** 2 + y ** 2) * dy * dx
        y += dy
    x += dx

print(integral)

integral = 0
x = a + dx
while x <= b:
    y = c + dy
    while y <= d:
        integral += -(x ** 2 + y ** 2) * dy * dx
        y += dy
    x += dx

print(integral)