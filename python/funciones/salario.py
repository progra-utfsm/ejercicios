# Calcular base considerando horas extra
def calcular_base(hrs, monto):
   if hrs > 44:
      normales = 44
      extra = hrs - 44
      if extra > 40:
         extra = 40
   else:
      normales = hrs
      extra = 0
   return monto * (normales + extra * 1.5)

# Tabla de impuestos
def calcular_monto_impuestos(imponible):
   if imponible <= 680022:
      return 0
   elif imponible <= 1511160:
      return imponible * 4 / 100 - 27200.88
   elif imponible <= 2518600:
      return imponible * 8 / 100 - 87647.28
   elif imponible <= 3526040:
      return imponible * 13.5 / 100 - 226170.28
   elif imponible <= 4533480:
      return imponible * 23/100 - 561144.08
   elif imponible < 6044640:
      return imponible * 30.4 / 100 - 896621.60
   elif imponible < 15615320:
      return imponible * 35 / 100 - 1174675.04
   return imponible * 40 / 100 - 1955441.04

# Salud y AFP
def salud(monto):
   return monto * 0.07

def afp(monto):
   return monto * (0.1 + 0.0127)

# Entrada
monto_por_hora = int(input('Monto por hora: $'))
hrs_trabajadas = int(input('Horas trabajadas: '))

# Calculos
imponible = int(round(calcular_base(hrs_trabajadas, monto_por_hora)))
descuentos_legales = salud(imponible) + afp(imponible)
base_tributable = imponible - descuentos_legales
impuestos = int(round(calcular_monto_impuestos(base_tributable)))
sueldo = int(round(base_tributable - impuestos))

# Salida
print("Imponible: $", imponible)
print("Descuentos legales: $", descuentos_legales)
print("Base tributaria: $", base_tributable)
print("Impuestos: $", impuestos)
print("Sueldo: $", sueldo)