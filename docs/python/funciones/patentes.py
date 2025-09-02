# Retorna la ultima letra, segun los formatos de las patentes
def f(p):
	if '-' in p:
		x = p[1] 
	else:
		x = p[3] 
	return x

def tiene_restriccion(patente, catalitico, dia):
    if catalitico: # Si el auto es catalitico
        ultimo = f(patente) # Obtenemos la ultima letra
        # Realizamos el filtro segun lo solicitado
        if ultimo <= "G":
            if dia == "LUNES":
                return True
        elif ultimo <= "N":
            if dia == "MIERCOLES":
                return True
        elif ultimo > "N":
            if dia == "VIERNES":
                return True
    else: # Si no es catalitico
        ultimo = patente[-1] # Obtenemos el ultimo digito
        # Realizamos el frilto segun las condiciones indicadas
        # Como ultimo es un string, podemos usar el 'in' para evitar condicionales extras.
        if dia == "LUNES" and ultimo in "0123":
            return True
        elif dia == "MIERCOLES" and ultimo in "456":
            return True
        elif dia == "VIERNES" and ultimo in "789":
            return True
    return False # Para cualquier otro caso no tiene restriccion

print(tiene_restriccion('CRTJ 32', True, 'LUNES'))
print(tiene_restriccion('ZZ-9999', False, 'VIERNES'))
print(tiene_restriccion('RX−2134', False , 'MIERCOLES'))