# Pirata

Un pirata escondió su valioso tesoro en algún punto $(a,b)$ del mapa cartesiano (con $a$, $b$ números enteros entre $0$ y $100$).
Diseñe un programa que genere un punto $a$, $b$ dentro del intervalo $[0,100]$ de manera aleatoria y pregunte el escondite del tesoro. Se debe adivinar la posición del tesoro solicitando una posición $(x, y)$. Si el lugar ingresado coincide con la ubicación del tesoro se muestra la frase `"Tesoro encontrado"` y el algoritmo termina. En caso contrario, se imprime a qué distancia del tesoro se encuentra el punto ingresado y se vuelve a leer otro posible lugar. Lea el valor de cada coordenada por separado.

## Ejemplo 

```
Ingrese x: 50 
Ingrese y: 50 
Tesoro a 26.93 
Ingrese x: 20 
Ingrese y: 60 
Tesoro a 5.0 
Ingrese x: 20 
Ingrese y: 55 
Tesoro a 7.07 
Ingrese x: 25 
Ingrese y: 60 
Tesoro encontrado
```

*Nota:* No se base en los valores el ejemplo ya que los valores $a$, $b$ son aleatorios y cambian en cada ejecución.

??? danger "Solución"
    ```python
    --8<-- "python/ciclos/pirata.py"
    ```