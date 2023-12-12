# Entrada de datos
n_amigos = int(input("Ingrese el número de amigos: "))
n_rolls = int(input("Ingrese el número de rolls: "))
n_piezas = int(input("Ingrese el número de piezas por roll: "))
# Cálculos
n_total = n_rolls * n_piezas
n_por_amigo = round(n_total / n_amigos, 2)
# Salida de datos
print("El número total de piezas por persona es:", n_por_amigo)
