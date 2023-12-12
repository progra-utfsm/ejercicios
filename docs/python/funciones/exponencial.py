# Calculo factorial
def factorial(n):
    prod = 1
    i = 1
    while i <= n:
        prod *= i
        i += 1
    return prod

# Función para calcular la aproximación
def aproximacion(N, x):
    n = 0
    exp = 0
    while n <= N:
        exp += (x ** n) / factorial(n)
        n += 1
    return exp

# Entrada de datos
N = int(input("Ingrese N: "))
x = float(input("Ingrese x: "))

# Cálculo de aproximación
exp_aprox = aproximacion(N, x)

# Salida con el resultado
print("Valor aproximacion:", exp_aprox)