N = int(input("Введите количество баллов: "))
if 80 <= N <= 100:
    print("Ваша оценка: 5")
elif 60 <= N <= 79:
    print("Ваша оценка: 4")
elif 40 <= N <= 59:
    print("Ваша оценка: 3")
elif N <= 40:
    print("Ваша оценка: 2")
else:
    print("Недопустимое значение")


