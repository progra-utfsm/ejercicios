# Funcion para contar
def contar(n):
    # Si n es 0 hay un digito
    if n == 0: 
        return 1
    else: # En otro caso
        i = 0
         # Dividimos por 10 mientras n > 0
        while n > 0:
            n //= 10
            i += 1 # Conteo de digitols
        return i

# Funcion para invertir 
def invertir(n):
    m = 0 # Variable a retornar
    while n > 0: # Repetimos mientras n sea mayor a 0 (podamos obtener resto distinto de 0)
        m = m * 10 + n % 10 # Generamos el con el digito de la derecha de n + 10 veces el m anterior 
        n //= 10 # Removemos el valor de la derecha
    return m

# Funcion capicua
def capicua(n):
    return n == invertir(n)

# Entrada
n = int(input("n: ")) 
# Salida
print("Dígitos:", contar(n))
print("Invertido:", invertir(n)) 
if capicua(n):
    print("Es capicua")
else:
    print("No es capicua")