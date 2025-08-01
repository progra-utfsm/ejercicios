# Entrada de datos  
a = int(input("Operando: ")) # Primer número real
o = input("Operador: ") # Operador tipo texto
b = int(input("Operando: ")) # Segundo número real

# Obtener resultado segun el operador
if o == "+":
    res = a + b
elif o == "-":
    res = a - b
elif o == "*":
    res = a * b
else:
    res = a / b

# Resultado
print(a, o, b, "=", res)