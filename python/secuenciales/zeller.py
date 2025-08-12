dd = int(input("Dia: "))
mm = int(input("Mes: "))
aaaa = int(input("Año: "))
a = (14 - mm) // 12
y = aaaa - a
m = mm + (12 * a) - 2
d = (dd + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12) % 7
print("d es:", d)