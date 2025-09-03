# Entrada de datos
m = int(input("Juegos ganados por A: "))
n = int(input("Juegos ganados por B: "))

# Condiciones
if (m == 6 and n < 5) or (m == 7 and n >= 5 and n < 7): # Casos en que gana A
    print("Gano A")
elif (n == 6 and m < 5) or (n == 7 and m >= 5 and m < 7): # Casos en que gana B
    print("Gano B")
elif (m < 7 and n < 7): # Si todavia nadie gana, y los valores son válidos, el juego sigue
    print("Aun no termina") 
else: # Otro resultado sería inválido
    print("Invalido")