def cuenta_minutos(viajes):
    c = {}
    for v in viajes:
        if viajes[v][1] not in c:
            c[viajes[v][1]] = 0
        c[viajes[v][1]] += viajes[v][2]
    final = []
    for i in c:
        final.append([i, c[i]])
    return final

viajes = {
  # identificador_viaje: [origen, destino, minutos]
  1323: ['santiago', 'lampa', 34],
  7643: ['santiago', 'vitacura', 27],
  9832: ['las condes', 'lampa', 45],
  2221: ['renca', 'las condes', 38],
  #...
}

print(cuenta_minutos(viajes))