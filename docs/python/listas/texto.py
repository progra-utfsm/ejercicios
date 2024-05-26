def texto_a_lista(texto):
    # Agregar un espacio al final del texto
    texto += ' '
    lista = []
    palabra = ''
    # Recorrer el texto
    for letra in texto:
        if letra == ' ': # Si la letra es un espacio
            lista.append(palabra.lower())
            palabra = '' # Limpiar la palabra
        else: # Si la letra no es un espacio
            if letra not in ',."()': # Evitar caracteres especiales
                palabra += letra
    return lista

def texto_a_lista_b(texto):
    palabras = texto_a_lista(texto)
    lista = [] # Lista para agregar los largos de las palabras
    for palabra in palabras:
        tmp = [len(palabra), palabra]
        lista.append(tmp)
    lista.sort()
    lista.reverse()
    salida = []
    for palabra in lista:
        salida.append(palabra[1])
    return salida

def texto_a_lista_c(texto):
    palabras = texto_a_lista(texto)
    sin_repetir = []
    for palabra in palabras:
        if palabra not in sin_repetir:
            sin_repetir.append(palabra)
    contador = []
    for palabra in sin_repetir:
        contador.append([palabras.count(palabra), palabra])
    contador.sort()
    contador.reverse()
    return contador

texto = '"Por qué será que en cuanto un hombre construye un muro, su vecino inmediatamente quiere saber qué hay del otro lado" (Tyrion Lannister). "Quien hace una pregunta debe ser capaz de soportar la respuesta" (Yoren)'

print(texto_a_lista(texto))
print(texto_a_lista_b(texto))
print(texto_a_lista_c(texto))