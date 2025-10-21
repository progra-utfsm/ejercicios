# Entrada de datos
segundos = int(input('Cantidad de segundos: '))

horas = segundos // 3600  # Cantidad de horas
segundos = segundos % 3600  # Segundos restantes
minutos = segundos // 60  # Cantidad de minutos
segundos = segundos % 60  # Segundos restantes

# Salida de datos 
print(horas,'horas,', minutos, 'minutos y', segundos, 'segundos')