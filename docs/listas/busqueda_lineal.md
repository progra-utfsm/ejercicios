# Búsqueda secuencial

La búsqueda secuencial (o lineal) es un método para encontrar un valor en una lista desordenada verificando cada elemento secuencialmente desde el primero hasta que el elemento buscado se encuentra o se llega al final de la lista.

Escriba la función `búsqueda_secuencial(lista, elemento)` que recibe una lista desordenada y un elemento que se desea encontrar. La función debe retornar la posición del `elemento` en la `lista` utilizando una búsqueda secuencial. Si no se encuentra retornar `False`.

## Ejemplos

```
>>> búsqueda_secuencial([11,23,58,31,56,77,43,12,65,19], 31)
3
>>> búsqueda_secuencial([11,23,58,31,56,77,43,12,65,19], 13)
False
```

??? danger "Solución"
    ```python
    --8<-- ";python/listas/busqueda_lineal.py"
    ```