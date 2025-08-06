# Entrada
d = int(input("Ingrese la distancia: "))
x = int(input("Ingrese  x: "))
y = int(input("Ingrese  y: "))
# Comprobar el cuadrante en el que se encuentra el punto
if abs(x) <= d and abs(y) <= d: # if x >= -d and x <= d and y >= -d and y= < d:
    print("Área 1")
elif abs(x) <= 2 * d and abs(y) <= 2 * d: # elif x >= -2 * d and x <= 2 * d and y >= -2 * d and y <= 2 * d:
    print("Área 2")
elif abs(x) <= 3 * d and abs(y) <= 3 * d: # elif x >= -3 * d and x <= 3 * d and y >= -3 * d and y <= 3 * d:
    print("Área 3")
elif abs(x) <= 4 * d and abs(y) <= 4 * d: # elif x >= -4 * d and x <= 4 * d and y >= -4 * d and y <= 4 * d:
    print("Área 4")
else:
    print("Fuera del área")