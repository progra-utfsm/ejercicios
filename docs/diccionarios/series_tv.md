# Series de TV

Para analizar datos de series de televisión se cuenta con la informacion de todas la series en una lista de listas en donde cada lista tiene la siguiente estructura: `[nombre, pais de origen, rating, generos]`. A su vez, generos es una lista con todos los generos a los cuales pertenece dicha serie. Por ejemplo:

```python
series = [
    ['Game of thrones','USA',9.4,['ficcion']],
    ['24','USA',8.4,['accion','suspenso']],
    ['La casa de papel','España',9.2,['accion','suspenso','drama']],
    ['Orange is the new black', 'USA', 8.5, ['comedia','drama']],
    ['Dark', 'Alemania', 9.2, ['ficcion','drama']],
    ['Sherlock','UK',9.2,['policial','drama','suspenso']],
    ['Merlı́','España',9.5,['drama']],
    ['Whitecollar','USA',8.2,['comedia','drama','suspenso']],
    ['Heroes','USA',7.7,['ficcion','accion']],
    ['Mistfit','UK',8.4,['accion','drama','ficcion']]
    # ...
]
```
Observe que la serie 24 es de USA, tiene un rating de 8.4 y está catalogada como de acción y suspenso.

## Ejercicios

(a) Escriba la función `series_por_genero(series)`, que recibe como parámetro la lista de series y retorna un diccionario en el que las llaves son los distintos géneros y los valores son los nombres de las series asociadas a cada género, ordenados alfabéticamente.

```python
>>> print(series_por_genero(series))
{
    'accion', ['24', 'Heroes', 'La casa de papel', 'Mistfit'],
    'comedia', ['Orange is the new black', 'Whitecollar'],
    'drama', ['Dark', 'La casa de papel', 'Merlı́', 'Mistfit', 'Orange is the new black', 'Sherlock', 'Whitecollar'],
    'ficcion', ['Dark', 'Game of thrones', 'Heroes', 'Mistfit'],
    'policial', ['Sherlock'],
    'suspenso', ['24', 'La casa de papel', 'Sherlock', 'Whitecollar']
}
```

(b) Escriba la función `paises_con_mas_series(series)`, que recibe como parámetro la lista de series y retorna una lista de `strings` con los nombres de los 3 paı́ses que tienen más series producidas, ordenada de mayor a menor de acuerdo al número de series. Puede suponer que siempre habrá suficientes paı́ses, y que no habrá empates entre los paı́ses en la cantidad de series. Utilice un diccionario para completar la tarea de contar.

```python
>>> print(paises_con_mas_series(series))
['USA', 'UK', 'España']
```

??? danger "Solución"
    ```python
    --8<-- "python/diccionarios/series_tv.py"
    ```