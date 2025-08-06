texto = input("Ingrese string: ") # Para el string con las notas
texto += ";" # Agregamos un punto y coma al final para que la última asignatura sea contada
info_asignatura = "" # Variable para guardar la información de la asignatura
mejor_asignatura = "" # Variable para guardar el nombre de la mejor nota
mejor_nota = -1 # Variable para guardar la mejor nota
suma = 0 # Variable para la sumatoria de notas 
contador = 0 # Contador de notas 
for c in texto: # Recorremos cada caracter del texto
    if c != ";": # Si no es un punto y coma, guardamos la información de la asignatura
        info_asignatura += c 
    else: # Si es un punto y coma, procesamos la información de la asignatura
        # Buscamos la posición del signo igual para separar el nombre de la asignatura de la nota
        pos_igual = 0  # Variable para guardar la posición del signo igual
        i = 0 # Variable para recorrer la información de la asignatura
        while i < len(info_asignatura): # Recorremos la información de la asignatura
            if info_asignatura[i] == "=": # Si encontramos el signo igual
                pos_igual = i # Guardamos la posición del signo igual
                i = len(info_asignatura) # Salimos del ciclo para evitar seguir buscando
            i += 1 # Aumentamos el contador para recorrer la información de la asignatura
        # Obtenemos el nombre de la asignatura y la nota
        nombre = info_asignatura[:pos_igual] 
        nota = int(info_asignatura[pos_igual+1:])
        info_asignatura = "" # Reiniciamos la información de la asignatura
        contador += 1 # Aumentamos el contador de notas
        suma += nota # Sumamos la nota a la sumatoria
        # Buscamos la mejor nota
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_asignatura = nombre
# Calculamos el promedio
promedio = round(suma / contador)
# Mostramos lo solicitado
print("Promedio:", promedio)
print("Mejor asignatura:", mejor_asignatura)