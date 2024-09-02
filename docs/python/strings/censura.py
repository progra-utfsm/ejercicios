texto = input("Ingrese un texto: ") # Texto a censurar
palabra = input("Ingrese una palabra: ") # Palabra a censurar
texto_censurado = "" # Variable para guardar el texto censurado
texto += " " # Agregamos un espacio al final para que la última palabra sea censurada
tmp = "" # Variable temporal para guardar las palabras
for letra in texto: # Recorremos cada letra del texto
    if letra != " ": # Si no es un espacio, guardamos la letra en la variable temporal
        tmp += letra 
    else: # Si es un espacio, procesamos la palabra
        if tmp.lower() == palabra.lower(): # Si la palabra es igual a la palabra a censurar
            texto_censurado += "#" * len(palabra) # Agregamos tantos "#" como letras tenga la palabra
        else: # Si la palabra no es igual a la palabra a censurar
            texto_censurado += tmp # Agregamos la palabra tal cual
        texto_censurado += " " # Agregamos un espacio al final de la palabra
        tmp = "" # Reiniciamos la variable temporal
print(texto_censurado) # Mostramos el texto censurado