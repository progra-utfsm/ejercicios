def validaADN(cadena):
    caracteres = "ACGT" # Caracteres validos
    i = 0 # Contador utilizado para verificar el grupo de 4 letras
    for c in cadena:
        if c == "-" and i == 5: # Si encuentra un guion, verificar que sea el 5to caracter
            i = 0 # Se reinicia el contador, para verificar el siguiente grupo
        else: # En caso contrario hay mas o menos de 4 bases
            return False
        if c not in caracteres: # Verificar si es un grupo de las 4 bases
            return False
        i += 1 # Contador para las bases
    return True
# Programa principal
n = int(input("Ingrese n: "))
i = 0 # Contador para las cadencas
cv = 0 # Contador de validas
cn = 0 # Contador no validas
while i < n:
    # Entrada de cadena
    cadena = input("Ingresar cadena: ")
    # Verificacion de cadena
    if validaADN(cadena):
        cv += 1
        print("Cadena valida")
    else:
        cn += 1
        print("Cadena no valida")
    i += 1
# Contador de cadenas validas e invalidas
print("Cadenas validas: ", cv)
print("Cadenas no validas:", cn)
