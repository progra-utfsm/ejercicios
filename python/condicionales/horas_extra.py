# Calcula el monto a pagar por concepto de horas extra
cat = int(input('Categoría del empleado (1-5): '))
horas = int(input('Horas totales trabajadas en la semana: '))
extra = horas - 44
if extra > 0: # Si hay horas extra
    if cat < 4:
        if extra > 10: # Limitar el maximo numero de horas extra a 10
            extra = 10
        # Verificar categoría    
        if cat==1:
            monto = 5000 * extra
        elif cat == 2:
            monto = 8000 * extra
        else:
            monto = 10000 * extra
        print('A pagar: $', monto)
    else:
        print('Por su categoría, no tiene derecho al pago de horas extra')
else:
    print('No trabajó horas extra esta semana')
