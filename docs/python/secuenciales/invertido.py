n = int(input("Ingrese número: ")) # Entrada de datos
d1 = n // 100 # Obtención del primer dígito
d2 = (n // 10) % 10 # Obtención del segundo dígito
d3 = n % 10 # Obtención del tercer dígito
n_inv = d3 * 100 + d2 * 10 + d1 # Se genera el número invertido
print(n_inv) # Salida de datos