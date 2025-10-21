# Función
def f(x):
    return x ** 2 - 2

# Derivada de función
def df(x):
    return 2 * x

# Método de Newton
def metodo_newton(x_0, N):
    n = 1 # Para controlar el número de iteraciones
    x = x_0 # Valor inicial
    while n <= N:
        x = x - f(x) / df(x)
        n += 1
    return x

# Entrada de datos
x_0 = float(input("Ingrese valor inicial: "))
N = int(input("Ingrese numero de iteraciones: "))

# Aproximación
sol = metodo_newton(x_0, N)

# Salida de datos
print("La raiz de 2 es aproximadamente:", sol)