# Robot

Un robot ha sido diseñado para moverse a lo largo de una cuadrícula, recibiendo como entrada alguna de las letras **N**, **S**, **E**, **O**, que le ordenan moverse un metro hacia el norte, sur, este, oeste, respectivamente. La letra **F** le pone fin al movimiento del robot. Escriba un programa que simule el movimiento el robot, leyendo letras ingresadas una por una. Al finalizar el movimiento, debe imprimir la distancia recorrida y la distancia de la ruta óptima (camino más corto posible para llegar al mismo destino).

Suponga que la cuadrícula se encuentra sobre un plano cartesiano, y el robot inicia mirando en dirección **N**.

## Ejemplo 

```
Movimiento: N
Movimiento: E
Movimiento: E
Movimiento: E
Movimiento: S
Movimiento: S
Movimiento: O
Movimiento: O
Movimiento: F
Distancia recorrida: 8 [m] 
Distancia óptima: 2 [m]
```

??? danger "Solución"
    ```python
    --8<-- "python/ciclos/robot.py"
    ```