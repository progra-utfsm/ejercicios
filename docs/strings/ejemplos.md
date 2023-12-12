# `Strings`

## General

Considere `frase = 'Solo vuela el que se atreve a hacerlo'`

1. ¿Cuál es la longitud de este string?
2. ¿Cuáles son los índices válidos?
3. ¿Cómo se expresa siempre el mayor índice en términos de la longitud?
4. ¿Cómo completaría el siguiente while para recorrer todos los índices del string?
    ```python
    i = 0
    while i < ???:
        i += 1
    ```

??? danger "Solución"
    1. $37$
    2. De $0$ a $36$ o de $-37$ a $-1$
    3. `len(frase) - 1`
    4. 
        ```python
        i = 0
        while i < len(frase):
            i += 1
        ```

## Casting

1. ¿Podemos convertir el string `"23515"` a un `int`? ¿cómo?
2. ¿Podemos hacer lo mismo con `"veintitrés mil quinientos quince"`?

??? danger "Solución"
    1. `int("23515")`
    2. No directamente.

## Tabla ASCII y orden lexicográfico

¿Cuál es el resultado de estas comparaciones?. Considere la [Tabla ASCII](https://ascii.cl/).

1. `'perro' < 'gato'`
2. `'perro' == 'Perro'`
3. `'perro' < 'Perro'` 

??? danger "Solución"
    1. `False`, `'p'` no está antes que `'g'`.
    2. `False`, diferencia la mayúscula.
    3. `False`, las mayúsculas van primero en ASCII.


## Inmutabilidad

1. ¿Qué imprime el siguiente programa?
    ```python
    nombre = 'Juan Carlos Bodoque'
    nombre.upper()
    print(nombre)
    ```
2. ¿qué hace esto? `print(nombre[3])`
3. ¿y esto? `nombre[3] = 'A'`

??? danger "Solución"
    1. `Juan Carlos Bodoque`. Para que tenga efecto el método utilizado hay que cambiar el código a:
        ```python
        nombre = 'Juan Carlos Bodoque'
        nombre = nombre.upper()
        print(nombre)
        ```
    2. `n`
    3. Produce un error. Los `strings` son **inmutables**.

## Pertenencia

¿Cuál es el resultado en las siguientes instrucciones?

1. 
    ```python 
    vocales = 'aeiou'
    'e' in vocales
    ```
2. `'E' in 'perro'`
3. `'pollo' in 'Vaca Pollo Cerdo Tomate Lechuga Repollo Zapallo'`

??? danger "Solución"
    1. `True`
    2. `False`
    3. `True`

## Recuperación de elementos

Suponga `texto = 'gato grande, negro y gordo'`

1. ¿Qué retorna `texto[4]`?
2. ¿`len(texto[5:8])`?
3. ¿`texto[:4]`?
4. ¿`texto[-5:]`?

??? danger "Solución"
    1. `' '`
    2. `3`
    3. `'gato'`
    4. `'gordo'`

## Recorrido de `strings`: `for`

1. ¿Qué realiza el siguiente programa?
    ```python 
    texto = 'gato grande, negro y gordo'
    for x in texto:
        if x in 'aeiou':
            print(x)
    ```
2.  ¿Cómo lo hacemos con `while` en vez de `for`?

??? danger "Solución"
    1. Muestra las vocales que hay en el texto.
    2. 
        ```python 
        texto = 'gato grande, negro y gordo'
        i = 0
        while i < len(texto):
            if texto[i] in 'aeiou':
                print(texto[i])
            i += 1
        ```
## Otros métodos para `strings`

### `replace` 

```python
texto.replace(buscado, nuevo)
```

Retorna un nuevo `string` a partir de `texto`, pero reemplazando todas las ocurrencias de `buscado` por `nuevo`. Si no existe,
retorna el `string` original `texto`.

#### Ejemplo

```python
texto = 'hola'
texto = texto.replace('o', 'x')
print(texto) # hxla
```

### `index`

```python
texto.index(buscado)
```

Retorna el índice de la primera ocurrencia de `buscado` dentro de `texto`. Si no existe produce un error.

#### Ejemplo

```python
print('hola mundo'.index('o')) # 1
```

## Métodos y funciones

La característica que diferencia a los métodos de las funciones es la forma de llamarlos. En una función aplicada a un `string`, como `len(s)`, se escribe el nombre de la función y el `string` va dentro de los paréntesis. En un método aplicado a un `string`, se comienza con el `string`, seguido de un punto, seguido del nombre del método y dentro de los paréntesis se incluyen parámetros adicionales.

## Ruteo

Rutear el siguiente programa para el texto: `'En un lugar de La Mancha'`. Indicar además,
con pocas palabras, la tarea que lleva a cabo.

```python
--8<-- "python/strings/ruteo.py"
```

