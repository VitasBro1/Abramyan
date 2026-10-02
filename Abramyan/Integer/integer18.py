chislo = int(input("Введите число: "))
if chislo < 999:
  print("Ошибка")
delenie = chislo // 1000 % 10
print(delenie)