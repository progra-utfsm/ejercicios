# Comentarios

## `print` y `return`

La función `print` muestra un valor numérico, texto u otro por pantalla, mientras que `return` no muestra nada,
solo retorna un valor donde la función haya sido llamada.

## Errores comunes

Veamos el siguiente ejemplo:

```python
# Retorna el MCD de dos números mediante el algoritmo de Euclides
def euclides(a, b): # Definicion de parametros
    a = input('a: ') # Sobreescribir parametros utilizando input
    b = input('b: ') # Lo mismo que arriba
    while b != 0:
        resto = a % b
        a = b
        b = resto
    print(a) # Deberiamos retornar en vez de solo mostrar
```

Comentarios:

- Es preferible evitar el uso de `input` al interior de una función.
- Generalmente la función finaliza con un `return` en vez de `print`. En algunos casos podríamos terminar sin retornar nada, pero no es tan común y depende de la aplicación.

## Orden de parámetros

Hay que tener presente el órden en que se definen los parámetros de una función y cómo se utilizarán posteriormente.
Por ejemplo: 

```python
def ecuacion_segundo_grado(a, b, c):
```

En este ejemplo el orden de los parámetros es importante, pues corresponde a los coeficientes de la
ecuación. Si se entregan en otro orden, se trata de otra ecuación.

## Confusión nombre de parámetros

Al momento de llamar una función, no importa el nombre de los "parámetros" sino que el órden de definición.
Por ejemplo:

```python
euclides(num1, num2)
```

```python
euclides(b, a)
```

## Tipo de datos

Aunque Python no restringe los parámetros por tipos, hay un contrato implícito para poder usar una función y eso incluye que los tipos deben corresponder.

## Capturar retorno

Si se define una función con retorno hay que asegurarse de capturar lo que se devuelva.
Ejemplo:

```python
euclides(9, 15)
```

debería ser

```python
m = euclides(9, 15)
```
si utilizamos `return`.

## Llamado de función

Al llamar a una función, el flujo del programa salta a la definición de la función, ejecuta el código
al interior de esta, y luego viene el retorno una vez que la función termina.

## `return`

La siguiente función entrega su resultado, pero también retorna al lugar donde fue llamada. Cualquier instrucción ubicada
después de `return` no se ejecutará nunca. Por eso funcionan códigos como este sin `else`:

```python
def es_par(n):
    if n % 2 == 0:
        return True
    return False
```

## Ejemplo

Considere la siguiente función:

```python
def mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c
```

- Siga la ejecución del llamado `mayor(1, 3, 2)` e indique lo que retorna
- Siga la ejecución del llamado `mayor(1, 2, 3)` e indique lo que retorna

## Secuencia de Collatz

El siguiente programa imprime en la pantalla la secuencia de Collatz desde un término inicial recibido como entrada. Estudie la implementación y muestre los valores que se imprimen si se ingresa $15$ como entrada. Preste atención al mecanismo de llamada y retorno de las funciones.

```python
def es_par(n):
    return n % 2 == 0

def termino_par(n):
    return n // 2

def termino_impar(n):
    return 3 * n + 1

t = int(input('t: '))
while t != 1:
    print(t)
    if es_par(t):
        t = termino_par(t)
    else:
        t = termino_impar(t)
print(t)
```

## Coeficiente binomial

Hacer ruteo de programa que calcula, usando funciones, el coeficiente binomial:

\begin{equation}
    {n \choose k} = \dfrac{n!}{k!(n-k)!}
\end{equation}

```python
def factorial(n):
    f = 1
    i = 2
    while i <= n:
        f *= i
        i += 1
    return f

def coeficiente_binomial(n, k):
    a = factorial(n)
    b = factorial(k)
    c = factorial(n-k)
    return a / (b * c)

coef = coeficiente_binomial(3, 2)
print(coef)
```