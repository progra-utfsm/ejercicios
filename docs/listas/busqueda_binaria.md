# Búsqueda binaria

La búsqueda binaria encuentra la posición de un elemento en una lista ordenada, comparando el elemento con el valor de al medio de la lista, si no son iguales, la mitad en la cual el valor no puede estar es eliminada y la búsqueda continúa en la mitad restante hasta que el valor se encuentre.

Por ejemplo, se desea encontrar el $10$ en la siguiente lista:

<table style="border: 1px solid black; font-size: 1em; float:center;">
    <tr>
        <td style="border-left: 1px solid; border-right: 1px solid black;">4</td>
        <td style="border-right: 1px solid black;">6</td>
        <td style="border-right: 1px solid black;">10</td>
        <td style="border-right: 1px solid black; background-color:  #eca1a6;">12</td>
        <td style="border-right: 1px solid black;">17</td>
        <td style="border-right: 1px solid black;">25</td>
        <td style="border-right: 1px solid black;">29</td>
    </tr>
</table>

Comparar el elemento buscado con el valor central: $10 < 12$, es menor, entonces descartar el lado derecho.

<table style="border: 1px solid black; font-size: 1em; float:center;">
    <tr>
        <td style="border-left: 1px solid; border-right: 1px solid black;">4</td>
        <td style="border-right: 1px solid black;">6</td>
        <td style="border-right: 1px solid black; background-color:  #eca1a6;">10</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
    </tr>
</table>

Comparar el elemento buscado con el valor central: $10 > 6$, es mayor, entonces descartar el lado izquierdo.

<table style="border: 1px solid black; font-size: 1em; float:center;">
    <tr>
        <td style="border-left: 1px solid; border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black; background-color:  #eca1a6;">6</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
        <td style="border-right: 1px solid black;">&nbsp;&nbsp;</td>
    </tr>
</table>

Comparar el elemento buscado con el valor central: $10 = 10$, es igual, entonces se encontró.

Si hubiesen sido distintos, como no quedan más elementos, el valor buscado no está en la lista.

Escriba la función `busqueda_binaria(lista, elemento)`que recibe una lista ordenada y un elemento que se desea encontrar. La función debe retornar `True` si encuentra el `elemento` en la `lista` utilizando una búsqueda binaria. Si no se encuentra retornar `False`.

## Ejemplos
```
>>> búsqueda_binaria([0, 1, 3, 8, 14, 18, 19, 34, 52], 3)
True
>>> búsqueda_binaria([0, 1, 3, 8, 14, 18, 19, 34, 52], 17)
False
```

??? danger "Solución"
    ```python
    --8<-- ";python/listas/busqueda_binaria.py"
    ```