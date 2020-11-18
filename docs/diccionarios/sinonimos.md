# Sinónimos

Se cuenta con un diccionario que asocia palabras con sinónimos

???info "Diccionario"
    ```python
    --8<-- "python/diccionarios/sinonimos_diccionario.py"
    ```

1. Escribir un programa que transforme un texto reemplazando las palabras que tienen sinónimo y dejando sin cambios las que no tienen. Se puede suponer que no hay signos de puntuación y que las palabras se separan con un único espacio en blanco, excepto la última que no tiene espacio al final. Puede utilizar el siguiente código como base:

```python
texto = 'En la penumbra vio su silueta con anteojos y un bonito cabello y sintió miedo y ganas de volver a su casa'
texto += ' '
palabra = ''
i = 0
while i < len(texto):
    if texto[i] == ' ':
        print(palabra) # Reemplazar esto con el procesamiento de la palabra
        palabra = ''
    else:
        palabra += texto[i]
i += 1
```
2. Construir un nuevo diccionario que incluya también los sinónimos en el orden inverso.

??? danger "Solución"
    ```python
    --8<-- "python/diccionarios/sinonimos.py"
    ```