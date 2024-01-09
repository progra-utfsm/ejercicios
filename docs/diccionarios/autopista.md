# Autopistas

Una concesionaria de autopista registra en la lista transitos las veces que cada vehículo pasa por uno de los pórticos de cobro. Cada lista de la lista contiene la patente del vehículo seguida del número de pórtico. Por ejemplo:

```python
transitos = [
    ['BBJJ77',2], ['CCHH19',3], ['AAFF37',3], ['BBJJ77',1], 
    ['AAFF37',1], ['DDKK33',3], ['AAFF37',1], ['AAFF37',2]
]
```

## Ejercicio 1

Escriba la función `mayor_movilidad(transitos)`, que retorna una lista de listas con los tres vehículos que pasaron por más pórticos. El primer elemento de cada lista es la patente y el segundo es la cantidad de pórticos por los que paso.

### Ejemplo
```python
>>> print(mayor_movilidad(transitos)) 
[['AAFF37', 4], ['BBJJ77', 2], ['DDKK33', 1]]
```

## Ejercicio 2

Escriba la función `reportar(transitos)`, que retorna un diccionario que lista, ordenadamente, los autos que pasaron por cada pórtico. La llave es el número de pórtico, y el valor es la lista de patentes, ordenada alfabeticamente y sin repeticiones.

### Ejemplo
```
>>> print(reportar(transitos))
{2: ['AAFF37', 'BBJJ77'], 3: ['AAFF37', 'CCHH19', 'DDKK33'], 1: ['AAFF37', 'BBJJ77']}
```


??? danger "Solución"
    ```python
    --8<-- "python/diccionarios/autopista.py"
    ```