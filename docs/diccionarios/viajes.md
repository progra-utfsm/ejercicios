# Viajes

Considerando la siguiente estructura:
```python
viajes = {
    # identificador_viaje: (origen, destino, minutos)
    1323: ('santiago', 'lampa', 34),
    7643: ('santiago', 'vitacura', 27),
    9832: ('las condes', 'lampa', 45),
    2221: ('renca', 'las condes', 38),
    #...
}
```

a) Desarrolle la función `cuenta_minutos(viajes)` que reciba el diccionario con la duración de
cada viaje, y entregue una lista con las comunas destino y los minutos totales que se han
demorado los viajes hacia ellas (en cualquier orden).
```python
>>> cuenta_minutos(viajes)
[('lampa', 79), ('vitacura', 27), ('las condes', 38)]
```

???danger "Solución"
    ```python
    --8<-- "python/diccionarios/viajes.py"
    ```