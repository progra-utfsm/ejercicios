# Cine

Usted desea ir al cine a ver la próxima película del estudio Marvel lo antes posible para evitar los molestos spoilers. Para ello la página del cine le muestra la lista sala con la disponibilidad de asientos. La sala del cine siempre será representada por una lista con $n$ listas, cada una de ellas con $n$ strings. Cada string puede tener los valores ``'O'`` que indica que el asiento está disponible o ``'X'`` que indica que está ocupado. 
El siguiente es un ejemplo para $n=5$. Nota: el valor de $n$ no debería ser importante.

```python
sala = [
    ["X","X","X","O","O"],
    ["X","X","X","X","O"],
    ["X","O","X","O","X"],
    ["X","X","X","X","O"],
    ["O","O","X","O","O"],
]
```

## Ejercicios

### Asientos disponibles

Escriba la función `asientos_disponibles(sala)` que indique si la sala del cine tiene asientos disponibles. La función debe retornar `True` si la sala tiene asientos disponibles y `False` en caso contrario.

```python
>>> asientos_disponibles(sala)
True
```

??? danger "Solución"
    ```python
    def asientos_disponibles(sala):
        for fila in sala:
            for asiento in fila:
                if asiento == 'O':
                    return True #encontramos algun asiento disponible
        return False #nunca encontramos un asiento disponible
    ```

### Disponible

Escriba la función `disponible(fila,columna,sala)` que reciba una sala del cine. La función debe retornar `True` si el asiento de la fila y columna ingresados está disponible y `False` en caso contrario. Si ingresa una fila o columna que no existan también deberá retornar `False`.

??? danger "Solución"
    ```python
    def disponible(fila, columna, sala):
        if fila >= 0 and fila < len(sala):
            if columna >= 0 and columna < len(sala[0]): 
                return sala[fila][columna] == "O"
            else:
                return False
        else:
            return False
    ```

```python
>>> disponible(2, 4, sala)
False
>>> disponible(10, 4, sala)
False
>>> disponible(0, 3, sala)
True
```

### Porcentaje Disponible

Escriba la función `porcentaje_disponible(sala)` que indique porcentualmente la disponibilidad de una sala de cine.

```python
>>> porcentaje_disponible(sala)
0.2
```

??? danger "Solución"
    ```python
    def porcentaje_disponible(sala):
        cantidad_asientos = 0
        cantidad_disponible = 0
        for fila in sala:
            for asiento in fila:
                if asiento == 'O':
                    cantidad_disponible+=1
                cantidad_asientos+=1
        return round(cantidad_disponible/cantidad_asientos,1)
    ```

### Espacio suficiente

Usted desea ir con sus $m$ amigos a ver la película y todos quieren ir a ver la película en la misma sala de cine. Debido al grán éxito en la pre-venta es posible que no queden muchos asientos. Escriba la función `hay_espacio_suficiente(m,sala)` que reciba un entero $m$ con la cantidad de amigos (usted incluido) que quieren ir a ver la película y la sala del cine. La función debe retornar `True` si hay espacio suficiente para que todos puedan ver la película en la sala de cine o `False` en caso contrario :(

```python
>>> hay_espacio_suficiente(12, sala)
False
>>> hay_espacio_suficiente(3, sala)
True
```

??? danger "Solución"
    ```python
    def hay_espacio_suficiente(m,sala):
        cantidad_disponible = 0
        for fila in sala:
            for asiento in fila:
                if asiento == 'O':
                    cantidad_disponible+=1
        if m <= cantidad_disponible:
            return True
        else:
            return False
    ```