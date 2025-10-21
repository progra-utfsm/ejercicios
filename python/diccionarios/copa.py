Chile = {
    1: 'Claudio Bravo',
    4: 'Mauricio Isla',
    17: 'Gary Medel',
    18: 'Gonzalo Jaro',
    15: 'Jean Beausejour',
    8: 'Arturo Vidal',
    21: 'Marcelo Díaz',
    20: 'Charles Aranguiz',
    6: 'José Pedro Fuenzalida',
    7: 'Alexis Sánchez',
    11: 'Eduardo Vargas'
}

Argentina = {
    1: 'Sergio Romero',
    4: 'Gabriel Mercado',
    17: 'Nicolás Otamendi',
    13: 'Ramiro Funes Mori',
    16: 'Marcos Rojo     ',
    6: 'Lucas Biglia',
    14: 'Javier Mascherano',
    19: 'Éver Banega',
    10: 'Lionel Messi',
    9: 'Gonzalo Higuaín',
    7: 'Ángel Di María'
}

# Preguntas #
# 1 y 2
nc = int(input("Ingrese número para jugador chileno: "))
if nc in Chile:
    print(Chile[nc])
else:
    print("No existe jugador con el número indicado")
na = int(input("Ingrese número para jugador argentino: "))
if na in Argentina:
    print(Argentina[na])
else:
    print("No existe jugador con el número indicado")
# 3
print("Alineación Chile")
for num in Chile:
    print("Con el número " + str(num) + ", " + Chile[num])
print("Argentina")
for num in Argentina:
    print("Con el número " + str(num) +  ", " + Argentina[num])

# 4
equipo = input("Indique el equipo (Chile o Argentina): ")
jugador = input("Indique el nombre del jugador: ")
if equipo == "Chile":
    for n in Chile:
        if Chile[n] == jugador:
            print("El número es:", n)
elif equipo == "Argentina":
    for n in Argentina:
        if Argentina[n] == jugador:
            print("El número es:", n)
else:
    print("Equipo inválido")

# 5
# Primero recuperamos los numeros de camiseta sin repetir
valores = []
for numero in Chile:
    valores.append(numero)
for numero in Argentina:
    if numero not in valores: # Utilizamos el condicional para no repetir numeros entre equipos
        valores.append(numero)
valores.sort() # Los ordenamos
# Ahora accederemos a los numeros de camiseta
for v in valores:
    # Mostramos solo las parejas que compartan numero de camiseta
    if v in Chile and v in Argentina:
        print("Con la camiseta " + str(v) + ": " + Chile[v] + ", " + Argentina[v])
