def f(x):
    d = set()
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sum(d)
for x in range(1000, 10000):
    if f(x) % 100 == 23:
        print(x, f(x))