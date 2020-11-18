# Números en diferentes idiomas

Como se dijo antes, los valores asociados a las llaves pueden ser colecciones, incluso diccionarios como en este caso.

```python
numeros = {
   'Francés': {1: 'un', 2: 'deux', 3: 'trois', 4: 'quatre', 5: 'cinq',
      6: 'six', 7: 'sept', 8: 'huit', 9: 'neuf', 10: 'dix'},
   'Portugués': {1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
      6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez'},
   'Inglés': {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
      6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'},
   'Español': {1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco',
      6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez'},
   'Italiano': {1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque',
      6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove', 10: 'dieci'},
   'Alemán': {1: 'eins', 2: 'zwei', 3: 'drei', 4: 'vier', 5: 'fünf',
      6: 'sechs', 7: 'sieben', 8: 'acht', 9: 'neun', 10: 'zehn'},
   'Mapudungún': {1: 'kiñe', 2: 'epu', 3: 'küla', 4: 'meli', 5: 'kechu',
      6: 'kayu', 7: 'regle', 8: 'pura', 9: 'aylla', 10: 'mari'}
}
```

Responda:

1. Determinar cómo se dice un número particular en un idioma en particular
2. Imprimir cómo se dice un número en todos los idiomas registrados
3. ¿Se puede determinar en qué idioma está un número en particular? ¿Qué cosas hay que tener en cuenta?

??? danger "Solución"
    ```python
    --8<-- "python/diccionarios/numeros.py"
    ```