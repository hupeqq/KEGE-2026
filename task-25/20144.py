def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = set()
    for i in range(2, int(num** .5) + 1):
        if num % i == 0 and prime(i):
            d |= {i}
        if num % (num // i) == 0 and prime(num // i):
            d |= {num // i}
    d = sorted(list(d))
    if len(d) > 1:
        r = max(d) - min(d)
        if r > 1000 and r % 3 == 0:
            return r
    return []
num = 3333338
cnt = 0
while cnt != 5:
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1
