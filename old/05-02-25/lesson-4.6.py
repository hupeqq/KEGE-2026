import random
num = int(input("Введите число: "))
num2 = random.randint(0, num)
ch1 = num2 / 9
ch2 = round(ch1, 3)
print(ch2)
