# Entrada de datos
c1 = int(input("Ingrese nota certamen 1: "))
c2 = int(input("Ingrese nota certamen 2: "))
nl = int(input("Ingrese nota laboratorio: "))
# Despejando la formula se obtien que c3 es
nc = int(round((60 - 0.3 * nl) / 0.7))
print(nc)
c3 = 3 * nc - (c1 + c2)
print(c3)
#Salida de datos
print("Necesita nota", int(round(c3)), "en el certamen 3")