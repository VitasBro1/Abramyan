A = float(input("Введите значение A: "))
C = float(input("Введите значение C: "))
B = float(input("Введите значение B: "))
if B < C:
 print("Введено неверное значение!")
if B < A:
 print("Введено неверное значение!")
elif  A < B and C > A and C < B:
 rast_ac = C - A
 rast_bc = B - C
 ymnoch = rast_ac * rast_bc
 print(ymnoch)
 # Время 21:29 Дата 13.09.26