# Para verificar si tiene una mayuscula o minuscula, o si corresponde a un digito,
# utilizamos la funcion ord(string) que nos entrega el codigo ASCII respectivo. 

def letra_mayuscula(caracter):
    # 65 corresponde a "A" y 90 a "Z". Se incluye la "Ñ"
    return (ord(caracter) >= 65 and ord(caracter) <= 90) or caracter == "Ñ"

def letra_minuscula(caracter):
    # 97 corresponde a "a" y 122 a "z". Se inlcuye la "ñ"
    return (ord(caracter) >= 97 and ord(caracter) <= 122) or caracter == 'ñ'

def digito(caracter):
    # 48 corresponde a "0" y 57 a "9"
    return ord(caracter) >= 48 and ord(caracter) <= 57 

def puntuacion(caracter):
    # Simplemente verificamos si se encuentra dentro del string con los caracteres de puntuacion
    return caracter in ",.;:"

def segura(password):
    # Esta propuesta analiza caracter por caracter y revisa si cumple los requisitos
    # Podemos revisar inmediatamente el largo, para evitar recorrer el string
    if len(password) < 8:
        return False
    else: # Si la contraseña es de al menos 8 caracteres, continuamos...
        # Inicializamos con variables falsas
        mayu = False
        minu = False
        digi = False
        punt = False
        # Recorremos los caracteres de la contraseña
        for c in password:
            # Aplicamos OR para saber si es que posee o no el criterio correspondiente
            mayu = mayu or letra_mayuscula(c)
            minu = minu or letra_minuscula(c)
            digi = digi or digito(c)
            punt = punt or puntuacion(c)
        # Luego de revisar todos los criterios, aplicamos AND a nuestras variables
        return mayu and minu and digi and punt
# Entrada
contra = input("Ingrese su contraseña: ")
# Salida
if segura(contra):
    print("Su contraseña es segura")
else:
    print("Su contraseña no es segura")

