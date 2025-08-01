from math import sin, cos

# Funcion a derivar
def f(x):
    return x * sin(x)

# Derivada de la funcion
def fp(x):
    return sin(x) + x * cos(x)

# Evaluar la funcion en una lista de valores
def evaluar_f(x):
    fx = list()
    for i in range(len(x)):
        fx.append(f(x[i]))
    return fx

# Evaluar la derivada en una lista de valores
def evaluar_fp(x):
    fpx = list()
    for i in range(len(x)):
        fpx.append(fp(x[i]))
    return fpx

# Cacular Diferencias finitas
def diferencias_finitas(x, dx, tipo):
    fd = list()
    N = len(x)
    fe = evaluar_f(x)
    # Calcular según el tipo de diferencias finitas
    if tipo == "adelantada":
        for i in range(N-1):
            fw = (fe[i+1] - fe[i]) / dx
            fd.append(fw)    
    elif tipo == "atrasada":
        for i in range(1, N):
            bw = (fe[i] - fe[i-1]) / dx
            fd.append(bw)
    elif tipo == "central":
        for i in range(1, N-1):
            cd = (fe[i+1] - fe[i-1]) / (2 * dx)
            fd.append(cd)
    return fd

# Calcular el error
def error(real, approx):
    err = 0
    for i in range(len(approx)):
        err += (real[i] - approx[i]) ** 2
    return err ** 0.5

# Solicitar datos
x_min = float(input("x min: "))
x_max = float(input("x max: "))
N = int(input("N: "))
tipo = input("Tipo: ")

# Crear lista de valores de x
x = list()
dx = (x_max - x_min) / (N - 1)
for i in range(N):
    x.append(x_min + i * dx)

# Calcular diferencias finitas y derivada exacta
fd = diferencias_finitas(x, dx, tipo)
fpe = evaluar_fp(x)

# Obtener valores de inicio y fin para el error
# Considerar que el error se calcula en los puntos interiores según el tipo de diferencias finitas
if tipo == "adelantada":
    i = 0
    f = N - 1
elif tipo == "atrasada":
    i = 1
    f = N
elif tipo == "central":
    i = 1
    f = N - 1

# Calcular error
error = error(fpe[i:f], fd)
print("Error:", error)