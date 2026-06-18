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
    d = sorted(list(d))
    if d:
        if (d[0] + d[-1]) % 100 == 63:
            if (d[0] + d[-1]) % len(d) == 0:
                return d[0] + d[-1]
    return 0
num = 7800001
cnt = 0
while cnt != 5:
    if res := f(num):
        print(num, res)
        cnt += 1
    num += 1