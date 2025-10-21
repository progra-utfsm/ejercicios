def crear_donantes(nombre_archivo):
    archivo = open(nombre_archivo, "w")
    archivo.write("15274,Fulana de Tal,200\n")
    archivo.write("15891,Jean Dupont,150\n")
    archivo.write("16443,Erika Mustermann,400\n")
    archivo.write("16504,Perico Los Palotes,80\n")
    archivo.write("17004,Jan Kowalski,200\n")
    archivo.close()

def mostrar(nombre_archivo):
    archivo = open(nombre_archivo)
    for linea in archivo:
        print(linea) # Mostramos cada linea del archivo
    archivo.close()

def monto(rut):
    archivo = open("donantes.txt")
    monto = 0 
    for linea in archivo:
        datos = linea.strip().split(",")
        if datos[0] == rut: # Si el rut es el que buscamos
            archivo.close() # Cerramos el archivo
            monto = int(datos[-1]) # Guardamos el monto
            return monto # Retornamos el monto
    # Si no encontramos el rut
    archivo.close() # Es necesario cerrar el archivo de todas maneras
    return monto # Retornamos 0 en este caso

def eliminar(rut):
    archivo = open("donantes.txt")
    lineas = list() # Lista para guardar los datos

    # Primero hay que leer el archivo
    for linea in archivo:
        datos = linea.strip().split(",")
        if datos[0] != rut: # Si no es el rut solicitado 
            lineas.append(linea) # Guardamos la linea completa
    archivo.close()

    # Ahora sobreescribimos el archivo pero sin la info que nos pidieron eliminar
    archivo = open("donantes.txt", "w")
    for l in lineas:
        archivo.write(l) # Guardamos las lineas que no contengan el rut solicitado
    archivo.close()

def agregar(rut, nombre, monto):
    info = list()
    info.append((rut, nombre, monto)) # Agregamos al nuevo donante
    # Leer el archivo
    archivo = open("donantes.txt")
    for linea in archivo: # Leer cada linea
        datos = linea.strip().split(",") 
        # Agregamos a los otros donantes en una lista de tuplas
        info.append((int(datos[0]), datos[1], datos[2])) 
    archivo.close()
    info.sort() # Ordenamos la lista por RUT

    archivo = open("donantes.txt", "w")
    for rut, nombre, monto in info: # Recorremos la lista con informacion
        archivo.write("{0},{1},{2}\n".format(rut, nombre, monto)) # Escribimos en el nuevo archivo
    archivo.close()
  

# Pruebas
crear_donantes("donantes.txt") # Pregunta 1
mostrar("donantes.txt") # Pregunta 2
print(monto('16504')) # Pregunta 3
eliminar('16504') # Pregunta 4
# Pregunta 5
rut = int(input("Ingresar rut: "))
nombre = input("Ingresar nombre: ")
monto = input("Ingresar monto: ")
agregar(rut, nombre, monto)
