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

# Función para mostrar una matriz
def mostrar_matriz(m):
    for fila in m:
        f = "" # Se crea un string vacio para visualizar la fila
        for e in fila:
            f += str(e) + " " # Se agrega un espacio para visualizar
        print(f)

# Función para calcular el producto matriz-matriz
def producto_matriz_matriz(A, B):
    n = len(A) # Se asume que A y B son matrices cuadradas
    C = [] # Se crea una "matriz" vacía para guardar el producto 
    for i in range(n): # Se recorre cada fila i
        fila = [] # Se crea una fila vacia para guardar los elementos de la fila i
        for j in range(n): # Se recorre cada columna j
            c = 0 # Se crea una variable para guardar el elemento c_ij
            for k in range(n): # Se recorre cada elemento k de la fila i y columna j
                c += A[i][k] * B[k][j]
            fila.append(c) # Se agrega el elemento c_ij a la fila
        C.append(fila) # Se agrega la fila a la matriz
    return C


# Solicitar n
n = int(input("Ingrese n: "))

# Crear vector y matriz
A = crear_matriz(n)
B = crear_matriz(n)

# Mostrar matrices
print("A: ")
mostrar_matriz(A)
print()
print("B: ")
mostrar_matriz(B)
print()

# Producto matriz-vector
print("AB: ")
AB = producto_matriz_matriz(A, B)

# Mostrar producto
mostrar_matriz(AB)