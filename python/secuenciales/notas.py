# Entrada de datos
c1 = int(input("Ingrese nota certamen 1: "))
c2 = int(input("Ingrese nota certamen 2: "))
nl = int(input("Ingrese nota laboratorio: "))
# Despejando la formula se obtien que c3 es
nc = (59.5 - 0.3 * nl) / 0.7 # Se utiliza 59.5 como equivalente a 60 por el redondeo que se realiza
c3 = 3 * nc - (c1 + c2) + 1 # Se añade + 1 para ajustar la parte decimal
# Por ejemplo no se puede obtener nota 45.123123, se requeriría un 46
#Salida de datos
print("Necesita nota", int(round(c3)), "en el certamen 3")