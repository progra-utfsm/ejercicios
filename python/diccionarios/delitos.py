calles = [
    # (id_calle1, nombre_calle1), …
    (883345, 'La Montana'), (321333, 'Miraflores'), (5843, 'Avellaneda'),
    (2283904, 'Del Valle'), (9430, 'Los Maitenes'), (2239102, 'Rio Tolten'),
    (9432, 'Teniente Bello')
]

niveles_peligrosidad = {
    # nivel: [id_calle1, id_calle2, id_calle3, …]
    2: [883345, 2283904, 5843],
    1: [9430, 2239102, 9432],
    # ...
}

delitos = [
    {'id_calle': 883345, 'fecha': '2015-03-23'},
    {'id_calle': 9432, 'fecha': '2015-02-12'},
    {'id_calle': 5843, 'fecha': '2015-03-21'},
    # ...
]

def agregar_delito(delito, delitos):
    id_calle, (anio, mes, dia) = delito
    #buscamos si la calle existe
    existe_calle = False
    for id, nombre in calles:
        if id_calle == id:
            existe_calle = True
    existe_nivel = False
    for n in niveles_peligrosidad:
        if id_calle in niveles_peligrosidad[n]:
            existe_nivel = True
    if existe_calle and existe_nivel:
        delitos.append({'id_calle': id_calle, 'fecha': '{}-{}-{}'.format(anio, mes, dia)})
        return True
    else:
        return False

def mes_mas_peligroso(anio, delitos):
    p = {}
    meses = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
        10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    for d in delitos:
        if int(d['fecha'][:4]) == anio:
            mes = int(d['fecha'][5:7])
            if mes not in p:
                p[mes] = 0
            p[mes] += 1
    r = []
    for i in p:
        r.append((p[i], i))
    r.sort()
    r.reverse()
    return meses[r[0][1]]