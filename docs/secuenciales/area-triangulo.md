# Área Triángulo

Realice un programa que calcule el área de un triángulo a partir de las longitudes de sus lados. Para calcularlo utilice la fórmula de Herón:

$$A = \sqrt{s\,(s-a)(s-b)(s-c)}$$

donde $a$, $b$ y $c$ son las longitudes de cada lado y $s=\dfrac{a+b+c}{2}$ es el semiperímetro.

??? danger "Solución"
	```python
	# Entrada de datos
	l1 = float(input("Ingrese longitud de lado 1: "))
	l2 = float(input("Ingrese longitud de lado 2: "))
	l3 = float(input("Ingrese longitud de lado 3: "))
	s = (l1 + l2 + l3) / 2 # semiperímetro
	d1 = s - l1 # diferencia1
	d2 = s - l2 # diferencia2
	d3 = s - l3 # diferencia3
	prod = s * d1 * d2 * d3 # producto de diferencias y semiperimetro
	area= prod ** (1 / 2) # raíz cuadrada ¿cómo se podría hacer lo mismo utilizando math.sqrt()?
	# Salida de datos
	print("El área del triángulo es", area)
	```
