# Entrada de datos
segundos = int(input('Cantidad de segundos: '))

minutos = segundos // 60 # Cantidad de minutos
segundos = segundos % 60 # Segundos restantes
horas = minutos // 60 # Cantidad de horas obtenidas si minutos >= 60
minutos = minutos % 60 # Minutos restantes

# Salida de datos 
print(horas,'horas,', minutos, 'minutos y', segundos, 'segundos')