entrada = input("Ingrese string: ") # Para el string con las notas
suma = 0 # Variable para la sumatoria de notas
mejor_materia = "" # Variable para guardar el nombre de la mejor nota
mejor_nota = -1 # Mejor nota
n_notas = 0 # Contador de notas
# La logica del programa es obtener la materia y nota e ir removiendola de la entrada
# Por lo tanto repetiremos el proceso hasta que se quiten todaslas materias y notas de la entrada
while len(entrada) > 0: 
    if ";" in entrada: # Si hay ';' en nuestra entrada podemos utilizar el metodo index para localizarlo
        i = entrada.index(";") # Indice para separar materia
        materia_nota = entrada[:i] # Obtenemos la materia con su nota
        # Removemos la materia y nota que ya procesamos. 
        # Se incluye el ';' para que no nos moleste en el procesamiento
        entrada = entrada.replace(materia_nota + ";", "")
    else: # Cuando a entrada no le queden ';', estamos en la materia del final
        materia_nota = entrada # La informacion de la materia se encuentra en la ultima parte de la entrada
        entrada = entrada.replace(materia_nota, "") # Se remueve la informacion (aqui entrada deberia quedar vacia)
    # Una vez tenemos el substring materia=nota, lo separamos utilizando '='
    j = materia_nota.index("=") # Indice para separar materia de la nota (utilizando el caracter '=')
    materia = materia_nota[:j] # Obtenemos el nombre de la materia
    nota = int(materia_nota[j+1:]) # Obtenemos la nota y la convertimos a entero. El +1 es para evitar el '='
    suma += nota # Sumatoria de notas
    n_notas += 1 # contador notas
    # Buscamos la major nota
    if nota > mejor_nota:
        mejor_materia = materia
        mejor_nota = nota
# Calculamos el promedio
promedio = int(round(suma / n_notas)) 
# Mostramos lo solicitado 
print("Promedio:", promedio)
print("Mejor asignatura:", mejor_materia)