# Fórmula 1

Los valores asociados con las llaves pueden ser también colecciones, como tuplas, listas e incluso otros diccionarios.

```python
F1 = {
   'Mercedes': ['Lewis Hamilton', 'Valtteri Bottas'],
   'Ferrari': ['Sebastian Vettel', 'Charles Leclerc'],
   'Red Bull Racing': ['Max Verstappen', 'Alexander Albon'],
   'McLaren': ['Carlos Sainz', 'Lando Norris'],
   'Renault': ['Daniel Ricciardo', 'Esteban Ocon'],
   'AlphaTauri': ['Pierre Gasly', 'Daniil Kvyat'],
   'Racing Point': ['Sergio Pérez', 'Lance Stroll'],
   'Alfa Romeo Racing': ['Kimi Räikkönen', 'Antonio Giovinazzi'],
   'Haas F1 Team': ['Romain Grosjean', 'Kevin Magnussen'],
   'Williams': ['George Russell', 'Nicholas Latifi']
}
```

Realice lo siguiente:

1. Imprimir los integrantes de un equipo particular.
2. ¿Cómo saber a qué equipo pertenece un piloto en particular?

??? danger "Solución"
    ```python
    --8<-- "python/diccionarios/formula1.py"
    ```