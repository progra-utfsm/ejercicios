anotaciones = input("Anotaciones: ") # Anotaciones del partido
anotaciones += " " # Agregamos un espacio al final para que el último periodo sea contado
total = 0 # Puntos totales
puntos = 0 # Puntos en el periodo actual
periodo = 1 # Periodo actual
# Recorremos cada caracter de las anotaciones
for c in anotaciones:
    if c == " ": # Si encontramos un espacio, termina el periodo
        print(puntos, "puntos en el periodo", periodo) # Imprimimos los puntos del periodo
        total += puntos # Sumamos los puntos del periodo al total
        periodo += 1 # Pasamos al siguiente periodo
        puntos = 0 # Reseteamos los puntos del periodo
    else: # Si no es un espacio, sumamos los puntos del periodo
        # Dependiendo del caracter (o tipo de puntos), sumamos los puntos correspondientes
        if c == "L": # Si es un tiro libre, sumamos 1 punto
            puntos += 1
        elif c == "D": # Si es un doble, sumamos 2 puntos
            puntos += 2
        elif c == "T": # Si es un triple, sumamos 3 puntos
            puntos += 3
# Al finalizar, imprimimos los puntos totales
print("Total:", total, "puntos")
    