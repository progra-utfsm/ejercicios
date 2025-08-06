# Entrada de datos
a = float(input("Ingrese longitud del lado a: "))
b = float(input("Ingrese longitud del lado b: "))
c = float(input("Ingrese longitud del lado c: "))

# Cálculos
s = (a + b + c) / 2 # semiperímetro
d1 = s - a # diferencia1
d2 = s - b # diferencia2
d3 = s - c # diferencia3
prod = s * d1 * d2 * d3 # producto de diferencias y semiperimetro
area= prod ** (1 / 2) # raíz cuadrada ¿cómo se podría hacer lo mismo utilizando math.sqrt()?

# Salida de datos
print("El área del triángulo es", area)