# Entradas
# Fecha actual
print("Ingrese la fecha actual: ")
d2 = int(input("Ingrese día: "))
m2 = int(input("Ingrese mes: "))
a2 = int(input("Ingrese año: "))
# Fecha de nacimiento
print("Ingrese su fecha de nacimiento: ")
d1 = int(input("Ingrese día: "))
m1 = int(input("Ingrese mes: "))
a1 = int(input("Ingrese año: "))

# Transformar fechas a dias
f1 = a1 * 365 + m1 * 30 + d1
f2 = a2 * 365 + m2 * 30 + d2
# Calcular diferencia
dif = f2 - f1
a = dif // 365 # Obtener cantidad de años
m = (dif % 365) // 30 # Obtener cantidad de meses
d = (dif % 365) % 30 # Obtener cantidad de días

# Salida
print(a, m, d)