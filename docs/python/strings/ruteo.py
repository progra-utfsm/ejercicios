texto = input('Texto: ')
inicio = True
convertido = ''
for c in texto:
    if inicio:
        convertido = convertido + c.upper()
        inicio = False
    elif c == ' ':
        inicio = True
    else:
        convertido = convertido + c
print(convertido)