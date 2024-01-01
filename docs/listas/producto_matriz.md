# Producto matriz-vector

Sea $A\in\mathbb{R}^{n\times n}$ una matriz y $\mathbf{b}\in\mathbb{R}^n$ un vector, definidos como:

$$
A = 
\begin{pmatrix}
    a_{1,1} & a_{1,2} & \cdots & a_{1, n} \\
    a_{2,1} & a_{2,2} & \cdots & a_{2, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n,1} & a_{n,2} & \cdots & a_{n, n} \\
\end{pmatrix} \quad \text{y} \quad
\mathbf{b} = 
\begin{pmatrix}
    b_1 \\ b_2 \\ \vdots \\ b_n
\end{pmatrix}.
$$

El producto matriz-vector se calcula de la siguiente manera:

$$
A\,\mathbf{b} = 
\begin{pmatrix}
    a_{1,1} & a_{1,2} & \cdots & a_{1, n} \\
    a_{2,1} & a_{2,2} & \cdots & a_{2, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n,1} & a_{n,2} & \cdots & a_{n, n} \\
\end{pmatrix}
\begin{pmatrix}
    b_1 \\ b_2 \\ \vdots \\ b_n
\end{pmatrix}
= 
\begin{pmatrix}
    a_{1, 1}\,b_{1} + a_{1, 2}\,b_{2} + \dots + a_{1, n}\,b_{n} \\
    a_{2, 1}\,b_{1} + a_{2, 2}\,b_{2} + \dots + a_{2, n}\,b_{n} \\
    \vdots \\
    a_{n, 1}\,b_{1} + a_{n, 2}\,b_{2} + \dots + a_{n, n}\,b_{n} 
\end{pmatrix}
$$

o escrito de forma compacta

$$
A\,\mathbf{b} = 
\begin{pmatrix}
\sum_{i=1}^n a_{1, i}\,b_i \\
\sum_{i=1}^n a_{2, i}\,b_i \\
\vdots \\
\sum_{i=1}^n a_{n, i}\,b_i \\
\end{pmatrix}.
$$

Desarrolle un programa que calcule el producto matriz-vector para un valor de $n$ ingresado por usuario. El programa debe mostrar la matriz y el vector y finalmente el producto.

Puede generar la matriz $A$ y el vector $\mathbf{b}$ con valores aleatorios utilizando el siguiente código:

!!! example
    ```python
    from random import random

    def crear_vector(n):
        v = []
        for i in range(n):
            v.append(random())
        return v

    def crear_matriz(n):
        m = []
        for i in range(n):
            m.append(crear_vector(n))
        return m
    ```

## Ejemplo

```
Ingrese n: 4
A: 
0.29897956887511123 0.4854449886464737 0.6208100585958172 0.09177889843579046 
0.9185016249163171 0.9914276017940338 0.11848324268473831 0.6943613227580757 
0.5430249582511094 0.16139741654489315 0.5672829232809159 0.5307077861481704 
0.39333373239457714 0.6079569057108376 0.023416842116470327 0.012533574907011902 

b: 
0.13577465224021967
0.32505790640569954
0.272909157229402
0.4923975548377869

Ab: 
0.41300803374191936
0.8212175987039882
0.5423284519216363
0.2635881219700423
```


??? danger "Solución"
    ```python
    --8<-- "python/listas/matriz_vector.py"
    ```


# Producto matriz-matriz

Sean $A, B\in\mathbb{R}^{n\times n}$  matrices definidas como:

$$
A = 
\begin{pmatrix}
    a_{1,1} & a_{1,2} & \cdots & a_{1, n} \\
    a_{2,1} & a_{2,2} & \cdots & a_{2, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n,1} & a_{n,2} & \cdots & a_{n, n} \\
\end{pmatrix} \quad \text{y} \quad
B = 
\begin{pmatrix}
    b_{1,1} & b_{1,2} & \cdots & b_{1, n} \\
    b_{2,1} & b_{2,2} & \cdots & b_{2, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    b_{n,1} & b_{n,2} & \cdots & b_{n, n} \\
\end{pmatrix}.
$$

El producto de matrices se calcula de la siguiente manera:

$$
\begin{split} 
A\,B &=
\begin{pmatrix}
    a_{1,1} & a_{1,2} & \cdots & a_{1, n} \\
    a_{2,1} & a_{2,2} & \cdots & a_{2, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n,1} & a_{n,2} & \cdots & a_{n, n} \\
\end{pmatrix}
\begin{pmatrix}
    b_{1,1} & b_{1,2} & \cdots & b_{1, n} \\
    b_{2,1} & b_{2,2} & \cdots & b_{2, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    b_{n,1} & b_{n,2} & \cdots & b_{n, n} \\
\end{pmatrix} \\[1em]
&= 
\begin{pmatrix}
    \sum_{i=1}^n a_{1, i}\,b_{i, 1} & \sum_{i=1}^n a_{1, i}\,b_{i, 2} & \dots & \sum_{i=1}^n a_{1, i}\,b_{i, n} \\
    \sum_{i=1}^n a_{2, i}\,b_{i, 1} & \sum_{i=1}^n a_{2, i}\,b_{i, 2} & \dots & \sum_{i=1}^n a_{2, i}\,b_{i, n} \\
    \vdots & \vdots & \ddots & \vdots \\
    \sum_{i=1}^n a_{n, i}\,b_{i, 1} & \sum_{i=1}^n a_{n, i}\,b_{i, 2} & \dots & \sum_{i=1}^n a_{n, i}\,b_{i, n}
\end{pmatrix}.
\end{split}
$$

Extienda su programa anterior o desarrolle uno nuevo para calcular el producto de matrices. 
El programa debe solicitar el valor de $n$, mostrar las matrices y luego el resultado. Puede generar las matrices con valores aleatorios utilizando el código de la sección anterior.

## Ejemplo

```
Ingrese n: 3
A: 
0.7579130713983545 0.7051866951144764 0.7093682532601882 
0.6835898432342268 0.5076784751826147 0.7544466570278985 
0.2875664351545816 0.10466389947529275 0.8882499269287549 

B: 
0.8871720889936138 0.06174559217119968 0.9311381318484788 
0.3335438666265823 0.11681278877449985 0.8556315217419117 
0.3278333631933946 0.34297234504926755 0.26754793936057886 

AB: 
1.1401646000190586 0.37246630919492857 1.4988917408659321 
1.0231276557758922 0.36026633733502067 1.272752924301118 
0.5812288776290825 0.33462720223749903 0.5949672423786242 
```

??? danger "Solución"
    ```python
    --8<-- "python/listas/matriz_matriz.py"
    ```