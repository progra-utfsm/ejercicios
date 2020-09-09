from math import pi

# Entradas
radio = float(input('Radio: '))
altura = float(input('Altura: '))

# Cálculos
area_base = pi * radio ** 2
perimetro_base = 2 * pi * radio
volumen_cilindro = area_base * altura
area_bases_cilindro = 2 * area_base
area_lateral_cilindro = perimetro_base * altura
area_total_cilindro = area_bases_cilindro + area_lateral_cilindro

# Salidas 
print('Area bases:', area_bases_cilindro)
print('Area lateral:', area_lateral_cilindro)
print('Area total:', area_total_cilindro)
print('Volumen:', volumen_cilindro)