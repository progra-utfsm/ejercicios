texto = input("Ingrese un texto: ")
palabra = input("Ingrese una palabra: ")
texto_censurado = ""
texto += " "
tmp = ""
for letra in texto:
    if letra != " ":
        tmp += letra 
    else:
        if tmp.lower() == palabra.lower():
            texto_censurado += "#" * len(palabra)
        else:
            texto_censurado += tmp
        texto_censurado += " "
        tmp = ""
print(texto_censurado)