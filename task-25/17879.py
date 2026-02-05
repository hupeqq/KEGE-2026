def f(x):
    d = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    d = list(d)
    if len(d) > 1:
        m = max(d) + min(d)
        if m % 10 == 4:
            return m
    return 0
num = 800001
cnt = 0
while cnt !=5:
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1
