# Fechas mágicas

Una fecha mágica es una fecha en la que el día multiplicado por el mes es igual a los últimos dos dígitos del año. Por ejemplo, el 10 de junio de 1960 es una fecha mágica, pues junio es el mes 6, y al multiplicarlo por 10 el resultado coincide con el año: 60. Escriba una función que determine si una fecha es mágica o no, retornando True o False según corresponda. La fecha que recibe la función es un string en formato "mes dia, año", con un espacio separando el mes y el día, y una coma y un espacio separando el año. Por ejemplo, “Junio 10, 1960”. Puede utilizarse, una función que convierte un mes escrito en palabras a su equivalente en número entero.

??? danger "Solución"
    ```python
    --8<-- "python/strings/fechas.py"
    ```