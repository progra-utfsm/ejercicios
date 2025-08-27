# Ruteos

## Ejercicio 1

Se cuenta con un programa que suma los gastos en que una persona incurrió durante un viaje (cuando se podía viajar). Como no se sabe de antemano la cantidad de gastos, el programa termina cuando se ingresa un $0$ (o un valor negativo).

(a) Rutear el siguiente programa, para $100$, $500$, $200$, $0$.

```python
total = 0
gasto = int(input('Ingrese un gasto (0 para terminar): '))
while gasto > 0:
    total += gasto
    gasto = int(input('Ingrese un gasto (0 para terminar): '))
print('Total de gastos:', total)
```

(b) Analizar la siguiente forma alternativa de implementar la solución, que usa un flag.

```python
total = 0
continuar = True
while continuar:
    gasto = int(input('Ingrese un gasto (0 para terminar): '))
    if gasto <= 0:
        continuar = False
    else:
        total += gasto
print('Total de gastos:', total)
```

## Ejercicio 2

Rutear el siguiente programa, para $n = 30$. Cada vez que se ejecuta `randint`, inventar un número en el rango apropiado.

```python
from random import randint
n = int(input('n: '))
cont = 0
while n > 0:
    t = randint(1,n)
    print(t)    
    n -= t
    cont += 1
print(cont, 'terminos')
```