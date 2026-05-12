def f(x):
    d = set()
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return d
def fact(x):
    d = []
    while x % 2 == 0:
        d.append(2)
        x //= 2
    i = 3
    while i * i < x + 1:
        while x % i == 0:
            d.append(i)
            x //= i
        i += 2
    if x > 2:
        d.append(x)
    return d
num = 5200001
cnt = 0
while cnt != 5:
    if len(f(num)) % 90 == 0 and len(fact(num)) == 9:
        print(num, max(fact(num)))
        cnt += 1
    num += 1
