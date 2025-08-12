def eliminar(texto, palabra):
    # Podemos simplemente retornar el resultado de un replace de la palabra por texto vacio
    # Se concatena un espacio a la palabra para borrar el espacio extra
    return texto.replace(palabra + " ", "")
# Entrada de datos
texto = input("Ingresar texto: ")
palabra = input("Ingresar palabra a eliminar: ")
# Salida
print("Nuevo texto:", eliminar(texto, palabra))