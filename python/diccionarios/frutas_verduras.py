total = 0
bolsa = []
for elemento in compras:
    if elemento in verdulería:
        lista = verdulería[elemento]
        if lista[1] > 0:
            bolsa.append(elemento)
            total += lista[0]
            lista[1] -= 1
        else:
            print('No hay', elemento)
    else:
        print('Negocio no vende', elemento)
print(bolsa)
print(total)