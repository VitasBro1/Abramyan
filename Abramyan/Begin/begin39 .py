A = float(input("Введите значение A: "))
B = float(input("Введите значение B: "))
C = float(input("Введите значение C: "))
D = B ** 2 - 4 * A * C
if D > 0:
    x = (-B + D ** 0.5) / (2 * A)
    x1 = (-B - D ** 0.5) / (2 * A)
    print (round(x , 2), round(x1 , 2))
elif D == 0:
    x2 = -B / (2 * A)
    print (round(x2 , 2))
else:
    print ("Нет корней!")
    # Время 23:53 Дата 13.09.26