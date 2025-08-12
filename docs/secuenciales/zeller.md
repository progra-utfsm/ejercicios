# Congruencia de Zeller

La Congruencia de Zeller es un algoritmo que permite calcular el dı́a de la semana de cualquier fecha del
calendario. Para una fecha `dd/mm/aaaa`, aplicamos las siguientes fórmulas, en donde todas las divisiones
deben producir números enteros como resultado:

$$
a = \dfrac{14 − mm}{12}
$$
$$
y = aaaa − a
$$
$$
m = mm + (12 \times a) - 2
$$
$$
d = \left(dd + y + \dfrac{y}{4}-\dfrac{y}{100}+\dfrac{y}{400}+\dfrac{31\times m}{12}\right)\bmod 7
$$
El dı́a resultante, $d$, es un número entre $0$ y $6$, donde $0$ representa domingo.

Desarrolle un programa que reciba el día, mes y año y retorne el valor de $d$.

### Ejemplo
```
Día: 12
Mes: 08
Año: 2025
d es: 2
``` 


?? danger "Solución"
    ```python
    --8<-- "python/secuenciales/zeller.py"
    ```