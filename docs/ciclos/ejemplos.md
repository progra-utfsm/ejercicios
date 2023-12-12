# Ejemplos

## Operadores de incremento

* `+=`
* `-=`
* `*=`
* `/=`
* `//=`
* `%=`

Utilizar `a += b` es equivalente a escribir `a = a + b`. El uso de los otros operadores es análogo, por ejemplo, `a *= b`       equivale a `a = a * b`... 

## ¿Qué realizan los siguientes códigos?

### ¿Cuántas veces se ejecuta este ciclo?

```python
i = 0
while i < n:
    print(i)
```

??? danger "Solución"
    Es un ciclo infinito ya que no se modifica `i`.

### ¿Qué realiza este ciclo?

```python
i = 0
while i < n:
    print(i)
    i += 1
```

??? danger "Solución"
    Se ejecuta `n` veces, desde `0` hasta `n-1`.

### ¿Qué realiza este ciclo?

```python
i = 1
while i <= n:
    print(i)
    i += 1
```

??? danger "Solución"
    También se ejecuta `n` veces, pero desde `1` hasta `n`.

### ¿Cuántas veces se ejecuta el siguiente ciclo?, ¿Para qué sirve?

```python
n = input('n: ')
while n <= 0:
    n = input('n: ')
```

??? danger "Solución"
    Se ejecutará tantas veces como se ingresen valores negativos. Sirve para asegurar el ingreso de $n \geq 0$. 

### ¿Qué problema tiene? ¿Cómo lo arreglamos?
El siguiente ciclo intenta imprimir todos los números impares entre $1$ y $100$:

```python
i = 1
while i != 100:
    print(i)
    i += 2
```

??? danger "Solución"
    El problema es que se salta la condición del `while`. Se puede arreglar utilizando `while i <= 100`.

### ¿Qué problema tiene el siguiente programa?

```python
# Programa que suma 5 números
i = 1
while i <= 5:
    suma = 0
    num = int(input('Ingrese un número: '))
    i += 1
    suma += num
print(suma)
```
??? danger "Solución"
    El problema es la inicialización de `suma`, ya que se inicia en `0` en cada iteración.

### ¿Qué problema tiene el siguiente programa?

```python
# Programa que cuenta cuántos números pares se ingresan
i = 1
contador = 0
while i <= 50:
    num = int(input('Ingrese un número: '))
    if num % 2 == 0:
        contador += 1
i += 1
```

??? danger "Solución"
    El problema es que el incremento está fuera del ciclo.

### ¿Qué problema tiene el siguiente código?

```python
n = int(input('n: '))
i = 1
while i <= n:
    linea = str(i) + ': '
    while j <= n:
        linea = linea + str(i * j) + ' '
        n += 1
    print(linea)
```

Este programa debería imprimir una tabla cuadrada con los múltiplos hasta el
número ingresado como entrada, por ejemplo:

```
n: 5
1: 1 2 3 4 5
2: 2 4 6 8 10
3: 3 6 9 12 15
4: 4 8 12 16 20
5: 5 10 15 20 25
```

??? danger "Solución"
    ```python
    n = int(input('n: '))
    i = 1
    while i <= n:
        j = 1 # FALTABA
        linea = str(i) + ': '
        while j <= n:
            linea = linea + str(i * j) + ' '
            j += 1 # CORREGIDO: confundía n con j
        print(linea)
        i += 1 # FALTABA
    ```