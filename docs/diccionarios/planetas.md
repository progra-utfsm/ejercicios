# Planetas

Tiene una lista de listas con la información de algunos planetas: `[ distancia al sol en kms, diámetro ecuatorial en kms, período orbital en años Tierra, período de rotación en días Tierra, masa relativa a Tierra ]`.

```python
planetas = {
   'Mercurio': [57910000, 4880, 0.241, 58.6, 0.06],
   'Venus': [108200000,12000, 0.72, 243, 0.82],
   'Tierra': [149600000, 12756, 1, 1, 1],
   'Marte': [227940000, 6794, 1.52, 1.03, 0.11],
   'Júpiter': [778833000, 142984, 5.20, 0.414, 318],
   'Saturno': [1429400000, 120536, 9.55, 0.426, 95],
   'Urano': [2870990000, 51118, 19.22, 0.718, 14.16],
   'Neptuno': [4504300000, 49492, 30.66, 0.6745, 17.2]
}
```

Realice lo siguiente:

1. Imprimir los planetas en orden descendente de diámetro, es decir, del más grande al más pequeño.
2. Determinar el planeta con el menor período de rotación. 

??? danger "Solución"
    ```python
    --8<-- "python/diccionarios/planetas.py"
    ```