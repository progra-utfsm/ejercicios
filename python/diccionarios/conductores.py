def agrega_conductor(conductores, nuevo_conductor):
    username = nuevo_conductor[0]
    nombre = nuevo_conductor[1]
    puntaje = nuevo_conductor[2]
    marca = nuevo_conductor[3][0]
    modelo = nuevo_conductor[3][1]
    if username in conductores:
        return False
    conductores[username] = [nombre, puntaje, [marca, modelo]]
    return True


def elimina_conductor(conductores, username):
    if username not in conductores:
        return False
    del conductores[username]
    return True


def ranking(conductores):
    r = []
    for c in conductores:
        r.append([conductores[c][1], conductores[c][0]])
    r.sort()
    r.reverse()
    final = []
    for datos in r:
        puntaje = datos[0]
        nombre = datos[1]
        final.append((nombre, puntaje))
    return final


conductores = {
    'azambrano': ['Andres Zambrano', 5.6, ['Hyundai', 'Elantra']],
    'jojeda': ['Juan Ojeda', 1.1, ['Hyundai', 'Accent']],
    # ...
}

print(agrega_conductor(conductores,['fsoto', 'Fabiola Soto', 4.4, ['Peugeot', '308']]))
print(elimina_conductor(conductores, 'jojeda'))
print(elimina_conductor(conductores, 'pmunoz'))
print(ranking(conductores))