def f(x):
    d = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    if len(d) > 1:
        m = sum(d)//len(d)
        if m % 1000 == 313:
            return m
    return 0
num = 699999
cnt = 0
while cnt != 7:
    if f(num):
        print(num, f(num))
        cnt += 1
    num -= 1
