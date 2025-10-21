def obtener_notas(datos):
    notas = {} # Diccionario para almacenar las notas
    datos = datos.split(";") # Separar los datos por ";" para obtener cada estudiante
    for estudiante in datos: # Iterar sobre cada estudiante
        tmp = estudiante.split(":") # Separar el nombre de las notas
        nombre = tmp[0] # Nombre del estudiante
        notas_estudiante = tmp[1].split(",") # Separar las notas por ","
        notas[nombre] = [] # Inicializar la lista de notas para el estudiante
        for c in notas_estudiante: # Iterar sobre cada nota
            nota_curso = c.split("=") # Separar la nota del curso
            curso = nota_curso[0] # Curso
            nota = int(nota_curso[1]) # Nota (convertir a entero)
            notas[nombre].append([nota, curso]) # Agregar la nota a la lista del estudiante
            notas[nombre].sort() # Ordenar las notas de menor a mayor
    return notas

datos1 =  "Carlos Pérez:cálculo=85,física=92;María González:programación=74;José Ramírez:mecánica=68,cálculo=95,álgebra=81;Ana Torres:termodinámica=77,química=88,electricidad=91"
datos2 = "Luis Martínez:historia=90,geografía=85;Sofía López:biología=88,química=92,física=79;Miguel Sánchez:matemáticas=95"
print(obtener_notas(datos1))
print(obtener_notas(datos2))