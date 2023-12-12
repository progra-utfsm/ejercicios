# Entrada de puntos
x1 = float(input("Ingrese x1: "))
y1 = float(input("Ingrese y1: "))
x2 = float(input("Ingrese x2: "))
y2 = float(input("Ingrese y2: "))
# Cálculo de distancia
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# Mostrar resultado
print("La distancia entre los puntos es:", distancia)