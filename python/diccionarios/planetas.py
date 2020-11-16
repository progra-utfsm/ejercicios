planetas = {
   'Mercurio': (57910000, 4880, 0.241, 58.6, 0.06),
   'Venus': (108200000,12000, 0.72, 243, 0.82),
   'Tierra': (149600000, 12756, 1, 1, 1),
   'Marte': (227940000, 6794, 1.52, 1.03, 0.11),
   'Júpiter': (778833000, 142984, 5.20, 0.414, 318),
   'Saturno': (1429400000, 120536, 9.55, 0.426, 95),
   'Urano': (2870990000, 51118, 19.22, 0.718, 14.16),
   'Neptuno': (4504300000, 49492, 30.66, 0.6745, 17.2)
}


lista = []
for planeta in planetas:
   diametro, _, _, _ = planetas[planeta]
   lista.append((diametro, planeta))
lista.sort()
lista.reverse()
for _, planeta in lista:
    print(planeta)