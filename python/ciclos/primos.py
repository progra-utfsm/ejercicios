n = int(input("Ingrese un número: "))
es_primo = True
d = 2
while (d <= n // 2) and es_primo:
    if n % d == 0:
        es_primo = False
    d += 1
if es_primo:
    print(n, "es primo")
else:
    print(n, "es compuesto")