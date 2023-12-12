def cuota(h, n, i):
   r = i / (1200)
   m = h * r / (1 - (1 + r)**(-12 * n))
   return round(m, 2)

def monto_total(h, n, i):
   return round(n * 12 * cuota(h, n, i), 2)

def intereses_pagados(h, n, i):
   return round(monto_total(h,n,i) - h, 2)

def porcentaje_intereses(h,n,i):
   return round(100 * intereses_pagados(h,n,i) / h, 2)

# Datos
h = 50000000
n = 15
i = 4.75

# Preguntas 1-4
print(cuota(h,n,i))
print(monto_total(h,n,i))
print(intereses_pagados(h,n,i))
print(porcentaje_intereses(h,n,i))

# Pregunta 5
n = 10
while n <= 25:
   print(n, cuota(h,n,i), monto_total(h,n,i), porcentaje_intereses(h,n,i))
   n += 1
