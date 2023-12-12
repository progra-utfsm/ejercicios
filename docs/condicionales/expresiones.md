# Expresiones booleanas

## Ejemplos de transcripción

1. "Iré en bicicleta a comprar si no está lloviendo y si el negocio está a menos de 5 km"
    ```python
    clima != "Lluvia" and distancia < 5
    ```
2. "Hago deporte si es martes o jueves"
    ```python
    dia == "Martes" or dia == "Jueves"
    ```

## Leyes de Morgan

!!! quote "Lenguaje natural"
    - La negación de la conjunción es la disyunción de las negaciones.
    - La negación de la disyunción es la conjunción de las negaciones.

!!! abstract "Formalmente"
    - $\neg (a \land b) \iff (\neg a) \lor (\neg b)$
    - $\neg (a \lor b) \iff (\neg a) \land (\neg b)$

!!! example "`Python`"
    ```python
        not (a and b) == (not a) or (not b)
    ```
    ```python
        not (a or b) == (not a) and (not b)
    ```

### Ejemplos

1. Para ser presidente de Chile se debe ser chileno por nacimiento y mayor de $35$:
```python
nacionalidad == "chilena" and edad > 35
```

¿Cuándo no se puede ser presidente de Chile?

??? example "`Python`"
    ```python
    not (nacionalidad == "chilena") or not (edad > 35)
    nacionalidad != "chilena" or edad <= 35
    ```

2. Dejo de comer cuando ya no tengo comida en el plato o cuando no tengo hambre
```python
plato != 'comida' or not hambre
```

¿Cuándo sigo comiendo?

??? example "`Python`"
    ```python
    not (plato != 'comida') and not (not hambre)
    plato == "comida" and hambre
    ```


## Propiedades

Los operadores `and` y `or` tienen las mismas propiedades de asociatividad y distributividad que los operadores aritméticos `*` y `+`.

### Ejemplo

"Hago deporte si es martes o jueves y hay sol"

```python
(dia == "Martes" or dia == "Jueves") and clima == "Sol"
```
es equivalente a 
```python
(dia == "Martes" and clima == "Sol") or (dia == "Jueves" and clima == "Sol")
```
