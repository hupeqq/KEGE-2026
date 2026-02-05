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
        s = sum(d)
        if s % 145 == 0:
            return s
    return 0
num = 32500000
cnt = 0
while cnt != 7:
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1