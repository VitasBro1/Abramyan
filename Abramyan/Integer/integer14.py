A = int(input("Введите трехзначное число: "))
dev = A % 10
dele = A // 10 % 10
delenie = A // 100
print(f"Число: {dev}{delenie}{dele}")