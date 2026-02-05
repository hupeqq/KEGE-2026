def f(x):
    d = []
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            d.append(i)
            if x // i != x:
                d.append(x // i)
    return sum(d)//len(d)
cnt = 0
num = 770000
while cnt != 5:
    if f(num) % 100 == 12:
        print(num, f(num))
        cnt += 1
    num -= 1