dd = int(input('Ingrese día: '))
mm = int(input('Ingrese mes: '))
aaaa = int(input('Ingrese año: '))

esBisiesto = (aaaa % 4 == 0)
esBisiesto = esBisiesto and (aaaa%100 != 0 or aaaa % 400 == 0)

añoOk = aaaa >= 1800
mesOk = (mm > 0 and mm <= 12)
diaOk = (dd > 0 and dd <= 31)
if mm == 4 or mm == 6 or mm == 9 or mm == 11:
    diaOk = diaOk and (dd <= 30)
if mm == 2:
    if esBisiesto:
        diaOk = diaOk and (dd <= 29)
    else:
        diaOk = diaOk and (dd <= 28)
if añoOk and mesOk and diaOk:
    print('Fecha correcta')
else:
    print('Fecha incorrecta')