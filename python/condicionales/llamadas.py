# Entrada de código de zona
zona = int(input('Código de zona: ')) 

# Verificación de zona
if zona == 12:
    costo_minuto = 2
elif zona == 15:
    costo_minuto = 2.2
elif zona == 18:
    costo_minuto = 4.5
elif zona == 19:
    costo_minuto = 3.5
elif zona == 23:
    costo_minuto = 6
elif zona == 25:
    costo_minuto = 6
elif zona == 29:
    costo_minuto = 5
else:
    print('Zona inválida')
    costo_minuto = 0

# Si hay minutos para cobrar
if costo_minuto > 0:
    # Entrada de horario
    horario = input('Horario de la llamada (dia/noche): ')
    if horario != 'dia' and horario != 'noche': # Verificación de horario
        print('Horario inválido')
    else:
        # Entrada de cantidad de minutos
        minutos = int(input('Cantidad de minutos: '))
        if minutos <= 0:
            print('Minutos debe ser positivo')
        else:
            total = minutos * costo_minuto
            if horario == 'noche': # Aplicación del descuento
                total = total * 0.8
            print('Costo total:', total)
