A = int(input("Введите трехзначное число: "))
delenie = A // 100
dele = A // 10 % 10
dev =  A % 10
ymnoch = dele * dev * delenie
print(ymnoch)