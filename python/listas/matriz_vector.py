from random import random

# Función para crear un vector de n elementos con valores aleatorios
def crear_vector(n):
    v = []
    for i in range(n):
        v.append(random())
    return v

# Función para crear una matriz de n x n elementos con valores aleatorios
def crear_matriz(n):
    m = []
    for i in range(n):
        m.append(crear_vector(n))
    return m

# Función para mostrar un vector
def mostrar_vector(v):
    for e in v:
        print(e)

# Función para mostrar una matriz
def mostrar_matriz(m):
    for fila in m:
        f = "" # Se crea un string vacio para visualizar la fila
        for e in fila:
            f += str(e) + " " # Se agrega un espacio para visualizar
        print(f)

# Función para calcular el producto matriz-vector
def producto_matriz_vector(A, b):
    n = len(b)
    Ab = [] # Se crea un vector vacío para guardar el producto
    for i in range(n): # Se recorre cada fila i
        c = 0 # Se crea una variable para guardar el elemento c_i
        for j in range(n): # Se recorre cada elemento j de la fila i
            c += A[i][j] * b[j] # Se calcula el elemento c_i
        Ab.append(c) # Se agrega el elemento c_i al vector
    return Ab # Se retorna el vector


# Solicitar n
n = int(input("Ingrese n: "))

# Crear matriz y vector
A = crear_matriz(n)
b = crear_vector(n)

# Mostrar matriz
print("A: ")
mostrar_matriz(A)
print()

# Mostrar vector
print("b: ")
mostrar_vector(b)
print()

# Producto matriz-vector
Ab = producto_matriz_vector(A, b)

# Mostrar producto
print("Ab: ")
mostrar_vector(Ab)