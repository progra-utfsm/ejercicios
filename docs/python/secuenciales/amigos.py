# Entrada de datos
amigo1 = int(input("Primer amigo: "))
amigo2 = int(input("Segundo amigo: "))
amigo3 = int(input("Tercer amigo: "))
# Total. Redondeamos para que tenga sentido el resultado en precios
total = round((amigo1 + amigo2 + amigo3) / 3)
# Lo que debe cada amigo
debe1 = total - amigo1
debe2 = total - amigo2
debe3 = total - amigo3
# Salida de datos
print("Primer amigo debe:", debe1)
print("Segundo amigo debe:", debe2)
print("Tercer amigo debe:", debe3)