# Pregunta 1
def punto_en_recta(p, r):
	x, y = p # Desempaquetar punto (x, y)
	m, b = r # Desempaquetar recta (pendiente, intercepto)
	# Si un punto pertenece a la recta se cumple que x * m + b = y
	return y == x * m + b

# Pregunta 2
def son_paralelas(r1, r2):
	# Desempaquetar rectas
	m1, b1 = r1 
	m2, b2 = r2
	# Dos rectas son paralelas si tienen la misma pendiente y distinto intercepto (comentario en clases)
	return m1 == m2 and b1 != b2

# Pregunta 3
def recta_que_pasa_por(p1, p2):
	# Desempaquetar puntos
	x1, y1 = p1 
	x2, y2 = p2
	# Pendiente 
	m = (y2 - y1) / (x2 - x1)
	# Intercepto, basta despejar la ecuacion de la recta y = mx + b => b = y - mx
	b = y1 - m *x1 # Se puede hacer con x2, y2 tambien
	recta = (m, b) # Nueva recta
	return recta

# Pregunta 4
def punto_de_interseccion(r1, r2):
	if son_paralelas(r1, r2): # Rectas paralelas
		return None
	else:
		# Desempaquetar rectas
		m1, b1 = r1
		m2, b2 = r2
		# Se debe buscar el punto (x,y) igualando ambas ecuaciones
		# m1 * x + b1 = m2 * x + b2 
		# => x = (b2 - b1) / (m1 - m2) 	
		x = (b2 - b1) / (m1 - m2) 
		# y se puede obtener evaluando x en cualquiera de las rectas
		y = m1 * x + b1
		return (x, y)

# Pruebas #
# Pregunta 1
recta = (2, -1) # esta es la recta y = 2x - 1
print(punto_en_recta((2, 3), recta))
print(punto_en_recta((0, -1), recta))
print(punto_en_recta((1, 2), recta))

# pregunta 3
print(recta_que_pasa_por((-2, 4), (4, 1)))
# Verificacion sugerida
p1 = (-2, 4)
p2 = (4, 1)
r = recta_que_pasa_por(p1, p2)
print(punto_en_recta(p1, r) and punto_en_recta(p2, r))

# Pregunta 4
r1 = (2, 1)
r2 = (-1, 4)
print(punto_de_interseccion(r1, r2))