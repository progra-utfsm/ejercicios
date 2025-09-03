def par(n):
    return n % 2 == 0

def f_par(n):
    return n // 2

def f_impar(n):
    return 3 * n + 1

n = int(input("Ingrese n: "))
maximo = 1
pares = 0
impares = 1 # Considerando el 1
while n > 1:
    print(n)
    if par(n):
        n = f_par(n)
        pares += 1
    else:
        n = f_impar(n)
        impares += 1
    if n > maximo:
        maximo = n
print(n) # Imprime el 1 final
print("Máximo:", maximo)
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)