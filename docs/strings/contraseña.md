# Contraseña

Escriba una función que retorne `True` si una contraseña particular es suficientemente segura y `False` en caso contrario. Una contraseña se considera suficientemente segura si contiene al menos una letra mayúscula, al menos una minúscula, al menos un dígito, al menos un caracter de puntuación (punto, coma, punto y coma o dos puntos), y debe tener al menos longitud $8$.

??? danger "Solución"
    ```python
    --8<-- "python/strings/password.py"
    ```

Modifique la función anterior para que reciba como parámetro adicional la contraseña anterior. Agregue como condición para ser una contraseña segura que la nueva contraseña no debe ser similar a la anterior con $3$ o menos caracteres de tolerancia.