N = int(input("Ingrese N: ")) # Numero de elementos a guardar
lista = [] # Lista para guardar los valores
i = 0 # Contador para controlar los elementos
while i < N:
    # Entrada de valores
    n = int(input("Ingrese valor: ")) 
    lista.append(n) # Se agregan a la lista
    i += 1

# Ordenar lista
lista.sort() 
print(lista)

# Contar pares/impares con while
i = 0
n_pares = 0 # Contador de pares
n_impares = 0 # Contador de impares
while i < len(lista):
    if lista[i] % 2 == 0:
        n_pares += 1
    else:
        n_impares += 1
    i += 1
# Mostrar resultado
print("Pares:", n_pares)
print("Impares:", n_impares)
 
# Contar pares/impares con for 1
n_pares = 0 # Contador de pares
n_impares = 0 # Contador de impares
for valor in lista:
    if valor % 2 == 0:
        n_pares += 1
    else:
        n_impares += 1
    i += 1
# Mostrar resultado
print("Pares:", n_pares)
print("Impares:", n_impares)

# Contar pares/impares con for 2
n_pares = 0 # Contador de pares
n_impares = 0 # Contador de impares
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        n_pares += 1
    else:
        n_impares += 1
    i += 1
# Mostrar resultado
print("Pares:", n_pares)
print("Impares:", n_impares)


