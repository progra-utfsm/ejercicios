# Pregunta a)
def series_por_genero(series):
    d = {}
    for serie in series: # Recorrer series
        # Extraer información que ocuparemos
        titulo = serie[0]
        generos = serie[3]
        for genero in generos: # Recorrer generos
            # Uso de patrón de clasificación
            if genero not in d:
                d[genero] = []
            d[genero].append(titulo)
            d[genero].sort() # Ordenar las series por título
    return d

# Pregunta b)
def paises_con_mas_series(series):
    d = {}
    # Utilizamos el patrón para contar
    for serie in series:
        pais = serie[1]
        if pais not in d:
            d[pais] = 0
        d[pais] += 1
    lista = [] # Lista para ordenar los países con más series
    for pais in d:
        lista.append([d[pais], pais]) # Se crea la estructura [[cantidad de series, pais], ...]
        # Se crea de forma conveniente para ordenar por cantidad de series
    lista.sort() # Orden ascendente
    lista.reverse() # Orden descendente
    resultado = [] # Lista para guardar solo los países
    for info in lista[:3]:
        resultado.append(info[1]) # Solo guardar el nombre del país
    return resultado

series = [
    ['Game of thrones','USA',9.4,['ficcion']],
    ['24','USA',8.4,['accion','suspenso']],
    ['La casa de papel','España',9.2,['accion','suspenso','drama']],
    ['Orange is the new black', 'USA', 8.5, ['comedia','drama']],
    ['Dark', 'Alemania', 9.2, ['ficcion','drama']],
    ['Sherlock','UK',9.2,['policial','drama','suspenso']],
    ['Merlí','España',9.5,['drama']],
    ['Whitecollar','USA',8.2,['comedia','drama','suspenso']],
    ['Heroes','USA',7.7,['ficcion','accion']],
    ['Mistfit','UK',8.4,['accion','drama','ficcion']]
    # ...
]

# Pruebas
print(series_por_genero(series)) # Pregunta a)
print(paises_con_mas_series(series)) # Pregunta b)
