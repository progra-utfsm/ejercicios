# Datos #
verdulería = {
   'Brócoli': [900, 10],
   'Pimentón': [800, 5],
   'Limones': [1500, 0],
   'Lechuga': [700, 10],
   'Palta': [3800, 7],
   'Tomates': [1200, 20],
   'Pepino': [500, 0],
   'Zanahorias': [700, 12],
   'Zapallo italiano': [450, 8],
   'Papas': [950, 25],
   'Frutillas': [3400, 2],
   'Peras': [1500, 0],
   'Manzanas': [1600, 4],
   'Naranjas': [1800, 12],
   'Plátanos': [1100, 3],
   'Kiwis': [2800, 0],
   'Mandarinas': [2200, 4]
}

# Preguntas #
# 1, 2 y 3
producto = input("Ingrese nombre de producto: ")
if producto in verdulería:
    print("El precio de", producto, "es", verdulería[producto][0], "y su stock es", verdulería[producto][1])
else:
    print("No hay stock del producto")

# 4 
mayor_precio = -1
mas_caro = ""
for producto in verdulería:
    if verdulería[producto][0] > mayor_precio:
        mayor_precio = verdulería[producto][0]
        mas_caro = producto
print("El producto más caro es: ", mas_caro)

# 5 
compras = ['Manzanas', 'Mangos', 'Papas', 'Tomates', 'Pepino', 'Pimentón', 'Plátanos']
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