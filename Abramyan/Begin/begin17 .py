A = float(input("Введите значение A: "))
B = float(input("Введите значение B: "))
C = float(input("Введите значение C: "))
if C < B:
 print("Введено неверное значение!")
if B < A:
 print("Введено неверное значение!")
elif  A < B and C > A and B < C:
 rast_ac = C - A
 rast_bc = C - B
 sum = rast_ac + rast_bc
 print (rast_ac)
 print (rast_bc)
 print (sum)
# Время 21:22 Дата 13.09.26