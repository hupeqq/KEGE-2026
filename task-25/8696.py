def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True
def f(x):
    d = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    if len(d):
        m = sum(d)
        return m
    return 0
num = 1273548
cnt = 0
while cnt != 5:
    summa = f(num)
    if summa and prime(summa % 100000):
        print(num, summa)
        cnt += 1
    num += 1