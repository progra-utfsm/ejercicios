# Pitágoras

Escriba un programa que reciba como entrada las longitudes de los dos catetos $a$ y $b$ de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa $c$ del triangulo, dado por el teorema de Pitágoras: $c^2=a^2+b^2$.

```python
Ingrese cateto a: 7
Ingrese cateto b: 5
La hipotenusa es 8.6023252670426267
```

??? danger "Solución"
	```python
	# Entrada de datos
	a = int(input("Ingrese cateto a: "))
	b = int(input("Ingrese cateto b: "))
	c = (a ** 2 + b ** 2) ** 0.5 # Pitágoras
	# Salida de datos
	print("La hipotenusa es", c)
	```