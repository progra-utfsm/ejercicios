# Entrada de datos
inv = int(input("Inversion inicial: ")) # Inversion inicial
tasa = float(input("% tasa de descuento: ")) # Tasa
r = tasa / 100 # % a decimal
van = -inv 
n = 1 
while van < 0:
    # Entrada de flujo de dinero
    flujo = int(input("Flujo mes " + str(n) + ": "))
    # Calculo de formular
    van += flujo / (1 + r) ** n 
    # Aumentar el numero de mes
    n += 1 
    # Salida de datos
    print("VAN: ", int(van)) # VAN calculado. Se redondea y transforma en entero

