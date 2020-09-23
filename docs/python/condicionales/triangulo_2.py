# Entrada de lados de triangulo
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Comprobar si el triángulo es válido
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    # En el caso que sea válido, ver el tipo de triángulo
    if a == b and b == c:
        tipo = "equilatero"
    elif a == b or b == c or a == c:
        tipo = "isoceles"
    else:
        tipo = "escaleno"
    print("El triangulo es", tipo) # Salida de tipo de triángulo
else: # Triángulo inválido
    print("No es un triangulo valido.")