def prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True
def f(x):
    d = set()
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            if prime(i): d.add(i)
            if prime(x // i): d.add(x // i)
    if len(d) > 1:
        m = min(d) + max(d)
        if m > 2000 and m % 10 == 8:
            return m
    return 0
num = 1_200_000
cnt = 0
while cnt != 5:
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1