# Pregunta 1
def costo_total_paciente(rut):
    atenciones = open("atenciones.txt")
    costo = 0 # Variable para guardar el costo
    for linea in atenciones:
        datos = linea.strip().split(":") # Separamos los datos
        if rut == datos[0]: # Si es el rut que se consulta
            costo += int(datos[2]) # Sumamos el costo
    atenciones.close()
    return costo

# Pregunta 2
def pacientes_dia(dia, mes, año):
    pacientes = open("pacientes.txt")
    atenciones = open("atenciones.txt")
    ruts = []
    nombres = []
    # Recorremos las atenciones para obtener los ruts 
    for linea in atenciones: 
        datos = linea.strip().split(":")
        fecha = datos[1].split("-") # Separamos las fechas
        # Comparamos si corresponde a la fecha
        if int(fecha[0]) == dia and int(fecha[1]) == mes and int(fecha[2]) == año:
            if datos[0] not in ruts:
                ruts.append(datos[0]) # Guardamos el rut
    # Recorremos los pacientes 
    for linea in pacientes: 
        datos = linea.strip().split(":")
        # Revisamos si el rut del paciente esta en la estructura donde guardamos los ruts
        if datos[0] in ruts: 
            nombres.append(datos[1])
    # Cierre de archivos
    pacientes.close()
    atenciones.close()
    return nombres

# Pregunta 3
def separar_pacientes():
    # Abrir archivos
    pacientes = open("pacientes.txt")
    jovenes = open("jovenes.txt", "w")
    mayores = open("mayores.txt", "w")
    for linea in pacientes: # Leer lineas del archivo
        datos = linea.split(":")
        # Filtrar segun edad
        if int(datos[2]) < 30:
            jovenes.write(linea)
        elif int(datos[2]) > 60:
            mayores.write(linea)
    # Cierre de archivos
    pacientes.close()
    jovenes.close()
    mayores.close()

# Pregunta 4
def ganancias_por_mes():
    atenciones = open("atenciones.txt")
    ganancias = dict() # Diccionario para guardar informacion
    for linea in atenciones: # Recorremos las lineas del archivo
        datos = linea.split(":") # Separamos los datos
        fecha = datos[1].split("-") # Separamos la fecha
        mes_año = "-".join(fecha[1:]) # Solo nos quedamos con mes-año
        if mes_año not in ganancias: # Guardamos los montos en cada mes-año
            ganancias[mes_año] = 0
        ganancias[mes_año] += int(datos[2])
    atenciones.close()
    # Ordenemos la informacion por fecha utilizando una lista de tuplas
    lista = [] # [((año, mes), ganancia), ...] asi podemos ordenar la estructura rapidamente
    for mes_año in ganancias:
        fecha = mes_año.split("-") # Separamos mes y año
        tupla = ((int(fecha[1]), int(fecha[0])), ganancias[mes_año]) # Creamos la lista de tuplas
        lista.append(tupla)
    lista.sort() # Ordenara de forma ascendente por la fecha
    gan = open("ganancias.txt", "w")
    # Guardamos la informacion en el archivo
    for fecha, ganancia in lista:
        año, mes = fecha
        gan.write("{}-{}:{}\n".format(mes, año, ganancia))
    gan.close()

# Pruebas
print(costo_total_paciente('8015253-1'))
print(costo_total_paciente('14350739-4'))
print(pacientes_dia(2, 6, 2010))
print(pacientes_dia(23, 6, 2010))
separar_pacientes()
ganancias_por_mes()