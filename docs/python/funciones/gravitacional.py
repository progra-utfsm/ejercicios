# Definición de función
def cgu(masa1, masa2, radio):
    G = 6.67428e-11
    # Aplicar la fórmula
    fuerza = G * masa1 * masa2 / (radio ** 2) 
    return fuerza

# Entrada de datos
m1 = float(input('m1: '))
m2 = float(input('m2: '))
r = float(input('Distancia: '))

# Salida de datos llamando directamente la función dentro del print
print('La fuerza de atraccion es', cgu(m1, m2, r))