def calcular_promedio(alumnos):
    resultado = []
    for alumno in alumnos:
        nombre = alumno[0]
        notas = alumno[1:]  # Todas las notas (desde índice 1 en adelante)
        promedio = round(sum(notas) / len(notas))  # Promedio redondeado al entero más cercano
        # Agregar [nombre, promedio] a la lista resultado
        resultado.append([nombre, promedio])
    return resultado


def mejor_promedio(alumnos):
    # Primero calculamos los promedios
    promedios = calcular_promedio(alumnos)
    # Inicializamos con el primer alumno
    mejor_nombre = promedios[0][0]
    mejor_prom = promedios[0][1]
    # Buscamos el mejor promedio
    for alumno_promedio in promedios:
        nombre = alumno_promedio[0]
        promedio = alumno_promedio[1]
        if promedio > mejor_prom:
            mejor_prom = promedio
            mejor_nombre = nombre
    return mejor_nombre


# Lista de alumnos con sus notas
alumnos = [
    ['Alberto Gonzalez', 40, 30, 70],
    ['Francisca Almonacid', 100, 40],
    ['Pedro Reyes', 30, 50],
    ['Juan Campos', 30, 60, 30, 70],
    ['Andrea Zamora', 30]
]

# Prueba de calcular_promedio
promedios = calcular_promedio(alumnos)
print("Promedios de alumnos:", promedios)

# Prueba de mejor_promedio
mejor = mejor_promedio(alumnos)
print("Alumno con mejor promedio:", mejor)
