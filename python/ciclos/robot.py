# Posicion inicial 
x = 0
y = 0
# Distancia recorrida por el robot
dist = 0
# Variable para mantener los movimientos
mov = '' # Se inicializa vacia
# Mientras no se ingrese el caracter de detencion
while mov != 'F':
    # Entrada de movimientos
    mov = input('Movimiento: ')
    if mov =='N':
        y += 1
        dist += 1
    elif mov == 'S':
        y -= 1
        dist += 1
    elif mov == 'O':
        x -= 1
        dist += 1
    elif mov == 'E':
        x += 1
        dist += 1
# Utilizamos la distancia de Manhattan ya que nos movemos en una cuadrícula
# Se obtiene con la posicion final con respecto al origen
optima = abs(x) + abs(y)
# Distancias
print('Distancia recorrida:', dist, '[m]')
print('Distancia óptima:', optima, '[m]')
