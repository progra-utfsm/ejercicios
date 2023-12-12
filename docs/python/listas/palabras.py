def palabra_mas_larga(palabras):
    # Consideramos un string vacio como la palabra mas larga
    max_pal = ""
    # Recorremos la lista
    for palabra in palabras:
        # Comparamos los largos de palabra
        if len(palabra) > len(max_pal):
            max_pal = palabra # Asignamos la palabra mas larga que encontremos
    return max_pal

palabras = ["murcielago", "hola", "chao", "paralelepipedo", "perro", "gato", "elefante"] # Lista de ejemplo
print("Palabra mas larga:", palabra_mas_larga(palabras)) # Resultado