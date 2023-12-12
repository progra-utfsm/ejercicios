# Frutas y verduras

Se cuenta con un diccionario que asocia productos con una lista que contiene el precio y el stock.

```python
verdulería = {
   'Brócoli': [900, 10],
   'Pimentón': [800, 5],
   'Limones': [1500, 0],
   'Lechuga': [700, 10],
   'Palta': [3800, 7],
   'Tomates': [1200, 20],
   'Pepino': [500, 0],
   'Zanahorias': [700, 12],
   'Zapallo italiano': [450, 8],
   'Papas': [950, 25],
   'Frutillas': [3400, 2],
   'Peras': [1500, 0],
   'Manzanas': [1600, 4],
   'Naranjas': [1800, 12],
   'Plátanos': [1100, 3],
   'Kiwis': [2800, 0],
   'Mandarinas': [2200, 4]
}
```

Realice lo siguiente:

1. Determinar el precio de un producto en particular
2. Agregar condición para validar existencia
3. Determinar el stock de un producto en particular, indicando si no existe
4. Determinar el producto más caro de la verdulería
5. Suponga una lista de strings con las compras que se quieren hacer, por ejemplo: `compras = ['Manzanas', 'Mangos', 'Papas', 'Tomates', 'Pepino', 'Pimentón', 'Plátanos']`. Se había escrito un programa que procesaba la lista de compras, indicando también si algún producto no estaba disponible en la verdulería, ya sea porque no lo venden o porque no hay stock actualmente. Al finalizar imprimía una lista con las compras efectuadas y el monto total a pagar. Reconstruya el código a continuación, separando los números con un único espacio y utilizando guiones que anteceden a las instrucciones para denotar los niveles de indentación.

```python linenums="1"
compras = ['Manzanas', 'Mangos', 'Papas', 'Tomates', 'Pepino', 'Pimentón', 'Plátanos']
bolsa.append(elemento)
print(bolsa)
else:
total = 0
else:
total += lista[0]
for elemento in compras:
bolsa = []
lista[1] -= 1
print('Negocio no vende', elemento)
lista = verdulería[elemento]
if elemento in verdulería:
print(total)
print('No hay', elemento)
if lista[1] > 0:
```

???danger "Solución"
    ```python
    --8<-- "python/diccionarios/frutas_verduras.py"
    ```