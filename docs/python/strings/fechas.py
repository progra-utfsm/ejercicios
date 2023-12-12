# Transforma un mes de tipo string a entero
def numero_mes(mes):
    # Para simplificar la comparacion se transforma a minuscula
    mes = mes.lower() 
    # Se hace la comparacion mes a mes
    if mes == "enero": 
        return 1
    elif mes == "febrero": 
        return 2
    elif mes == "marzo": 
        return 3
    elif mes == "abril":
        return 4
    elif mes == "mayo":
        return 5
    elif mes == "junio":
        return 6
    elif mes == "julio":
        return 7
    elif mes == "agosto":
        return 8
    elif mes == "septiembre":
        return 9
    elif mes == "octubre":
        return 10
    elif mes == "noviembre":
        return 11
    elif mes == "diciembre":
        return 12

def fechas_magicas(fecha):
    # Extraccion de dia, mes y año utilizando subtrings
    i1 = fecha.index(" ") # Buscamos el primer espacio
    i2 = fecha.index(",") # Buscamos la coma
    mes = fecha[:i1] # Se extrae el substring del mes 
    mes = numero_mes(mes) # Luego se transforma con nuestra funcion a entero
    dia = fecha[i1+1:i2] # Se extrae el dia
    dia = int(dia) # Se transforma a entero
    año = fecha[-2:] # Para el año solo obtenemos los ultimos valores
    año = int(año) # Se transforma en entero
    return dia * mes == año

# Entrada de fecha
fecha = input("Ingrese fecha: ")
# Salida
if fechas_magicas(fecha):
    print("Es fecha magica")
else:
    print("No es fecha magica")
