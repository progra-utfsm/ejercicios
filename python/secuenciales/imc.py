# Entrada
pies = int(input('Altura [pies]: '))
pulgadas = int(input('Altura [pulgadas]: '))
lb = int(input('Peso [lb]: '))

# Cálculos
altura = pies * 0.3048 + pulgadas * 0.0254 # Altura a [m]
masa = 0.45359237 * lb # Peso a [kg]
imc = masa / altura ** 2 # IMC

# Salida
print(imc,'[kg/m2]')