# Entrada de strings
oracion = input("Ingrese una oración: ")
palabra_buscar = input("Ingrese una palabra: ")
# Algoritmo
palabra = ""
oracion = oracion + " " # Agregar un espacio al final para facilitar la búsqueda
cont = 0 # Contador para las repeticiones
i = 0 # Indice para recorrer el string
for c in oracion:
    if c != " ": # Mientras no se encuentre un espacio, se sigue formando la palabra
        palabra += c
    else: # Si se encuentra un espacio, se compara la palabra formada con la buscada
        if palabra == palabra_buscar:
            cont += 1 # Si son iguales, se incrementa el contador
        palabra = "" # Se reinicia la palabra para formar la siguiente
# Salida
print("La palabra", palabra_buscar, "aparece", cont, "veces en la oración.")
