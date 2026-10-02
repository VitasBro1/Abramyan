a = float(input("Введите значение a: "))
p = 3.14
if a >= 0 and a <= 2 * p:
    ygol = p * a / 180
    print (ygol)
elif a <= 0 and a > 360:
    print("Введенно неверное значение!")
    # Время 23:01 Дата 13.09.26