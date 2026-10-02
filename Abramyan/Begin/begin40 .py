A1 = float(input('Введите А1: '))
B1 = float(input('Введите В1: '))
A2 = float(input('Введите А2: '))
B2 = float(input('Введите В2: '))
C1 = float(input('Введите С1: '))
C2 = float(input('Введите С2: '))
D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D
print(round(x , 2) , round(y , 2))
# Время 23:58 Дата 13.09.26
