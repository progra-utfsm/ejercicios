def desviacion_estandar(valores):
    # Numero de elementos
    n = len(valores) 
    # Calculo del promedio
    promedio = sum(valores) / n
    lista = [] # Lista para guardar las diferencias al cuadrado
    for val in valores: # Se recorren los valores
        lista.append((val - promedio) ** 2) # Se agregan las diferencias al cuadrado
    desv = (sum(lista) / (n - 1)) ** 0.5 # Calculo de la desviacion
    return desv
# Pruebas
print(desviacion_estandar([1.3, 1.3, 1.3]))
print(desviacion_estandar([4.0, 1.0, 11.0, 13.0, 2.0, 7.0]))
print(desviacion_estandar([1.5, 9.5]))