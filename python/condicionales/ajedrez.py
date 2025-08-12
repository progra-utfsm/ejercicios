# Entrada de posición de piezas de ajedrez
fila_alfil = int(input("Fila alfil: "))
columna_alfil = int(input("Columna alfil: "))
fila_torre = int(input("Fila torre: "))
columna_torre = int(input("Columna torre: "))
# Comprobar si el alfil come a la torre
if abs(fila_alfil - fila_torre) == abs(columna_alfil - columna_torre):
    print("Alfil captura")
elif fila_alfil == fila_torre or columna_alfil == columna_torre:
    print("Torre captura")
else:
    print("Ninugna captura")