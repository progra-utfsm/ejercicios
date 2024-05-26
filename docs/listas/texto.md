# Texto

Considere el siguiente texto sacado de una buena serie de televisión:
```console
texto = '"Por qué será que en cuanto un hombre construye un muro, su
vecino inmediatamente quiere saber qué hay del otro lado" (Tyrion
Lannister). "Quien hace una pregunta debe ser capaz de soportar la
respuesta" (Yoren)'
```

## Ejercicios

a. Cree la función `texto_a_lista(texto)` que reciba la variable texto y retorne una lista con las palabras que componen ese texto. Note que las letras en el resultado van en minúscula y no debe considerar los símbolos coma, punto, paréntesis y doble comillas.
```python
>>> palabras = texto_a_lista_a(texto)
>>> print( palabras )
['por', 'qué', 'será', 'que', 'en', 'cuanto', 'un', 'hombre',
'construye', 'un', 'muro', 'su', 'vecino', 'inmediatamente', 'quiere',
'saber', 'qué', 'hay', 'del', 'otro', 'lado', 'tyrion', 'lannister',
'quien', 'hace', 'una', 'pregunta', 'debe', 'ser', 'capaz', 'de',
'soportar', 'la', 'respuesta', 'yoren']
```

b. Modifique la función `texto_a_lista(texto)` para que ahora retorne la lista de palabras ordenadas de acuerdo a largo (de mayor a menor).
```python
>>> palabras = texto_a_lista_b(texto)
>>> print( palabras )
['inmediatamente', 'respuesta', 'lannister', 'construye', 'soportar',
'pregunta', 'vecino', 'tyrion', 'quiere', 'hombre', 'cuanto', 'yoren', 'saber', 'quien', 'capaz', 'será', 'otro', 'muro', 'lado', 'hace', 'debe', 'una', 'ser', 'qué', 'qué', 'que', 'por', 'hay', 'del', 'un', 'un', 'su', 'la', 'en', 'de']
```

c. Modifique la función `texto_a_lista(texto)` para que retorne la lista de palabras ordenadas según el número de veces que aparecen (de mayor a menor). Considere el siguiente ejemplo de ejecución del programa. Note que el resultado consta de la lista de palabras no repetidas que aparecen en el texto, indicando el número de veces que éstas aparecen.
```python
>> palabras = texto_a_lista_c(texto)
>> print( palabras )
[[2, 'un'], [2, 'qué'], [1, 'yoren'], [1, 'vecino'], [1, 'una'], [1, 'tyrion'], [1,'su'], [1, 'soportar'], [1, 'será'], [1, 'ser'], [1,'saber'], [1, 'respuesta'], [1, 'quiere'], [1, 'quien'], [1, 'que'], [1, 'pregunta'], [1, 'por'], [1, 'otro'], [1, 'muro'], [1, 'lannister'], [1, 'lado'], [1, 'la'], [1, 'inmediatamente'], [1, 'hombre'], [1, 'hay'], [1, 'hace'], [1, 'en'], [1, 'del'], [1, 'debe'], [1, 'de'], [1, 'cuanto'], [1, 'construye'], [1, 'capaz']]
```

??? danger "Solución"
    ```python
    --8<-- "python/listas/texto.py"
    ```