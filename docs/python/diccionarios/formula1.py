F1 = {
   'Mercedes': ['Lewis Hamilton', 'Valtteri Bottas'],
   'Ferrari': ['Sebastian Vettel', 'Charles Leclerc'],
   'Red Bull Racing': ['Max Verstappen', 'Alexander Albon'],
   'McLaren': ['Carlos Sainz', 'Lando Norris'],
   'Renault': ['Daniel Ricciardo', 'Esteban Ocon'],
   'AlphaTauri': ['Pierre Gasly', 'Daniil Kvyat'],
   'Racing Point': ['Sergio Pérez', 'Lance Stroll'],
   'Alfa Romeo Racing': ['Kimi Räikkönen', 'Antonio Giovinazzi'],
   'Haas F1 Team': ['Romain Grosjean', 'Kevin Magnussen'],
   'Williams': ['George Russell', 'Nicholas Latifi']
}

# Preguntas #
# 1
equipo = input("Ingrese el equipo: ")
if equipo in F1:
    print("Los integrantes del equipo", equipo, "son: ")
    for integrante in F1[equipo]:
        print("- ", integrante)
else:
    print("El equipo no existe")
# 2
integrante = input("Ingrese integrante: ")
for equipo in F1:
    if integrante in F1[equipo]:
        print(integrante, "pertenece a", equipo)