# Entrada de datos
N = int(input("Ingrese N: "))
x = float(input("Ingrese x: "))

# Cálculo de aproximación
n = 0
exp = 0
while n <= N:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    exp += (x ** n) / factorial
    n += 1

# Salida con el resultado
print("Valor aproximacion:", exp)