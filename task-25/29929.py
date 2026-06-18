def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = []
    while num % 2 == 0:
        d.append(2)
        num //= 2
    i = 3
    while i * i < num + 1:
        while num % i == 0:
            d.append(i)
            num //= i
        i += 2
    if num > 2:
        d.append(num)
    if len(d) == 2 and len(set(d)) == 2:
        return d
    return []
primes = []
for i in range(3_800_000):
    if prime(i):
        primes.append(i)
num = 3700001
cnt = 0
while cnt != 5:
    res = sorted(f(num))
    if res:
        if primes.index(res[1]) - primes.index(res[0]) == 1:
            print(num, res[0] + res[1])
            cnt += 1
    num += 1


