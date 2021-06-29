conductores = {
    'azambrano': ('Andres Zambrano', 5.6, ('Hyundai', 'Elantra')),
    'jojeda': ('Juan Ojeda', 1.1, ('Hyundai', 'Accent')),
    # ...
}


def agrega_conductor(conductores, nuevo_conductor):
    username, nombre, puntaje, (marca, modelo) = nuevo_conductor
    if username in conductores:
        return False
    conductores[username] = (nombre, puntaje, (marca, modelo))
    return True


def elimina_conductor(conductores, username):
    if username not in conductores:
        return False
    del conductores[username]
    return True


def ranking(conductores):
    r = []
    for c in conductores:
        r.append((conductores[c][1], conductores[c][0]))
    r.sort()
    r.reverse()
    final = []
    for puntaje, nombre in r:
        final.append((nombre, puntaje))
    return final
