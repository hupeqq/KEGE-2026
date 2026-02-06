def f(x):
    d = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    d = sorted(list(d), reverse=True)
    if len(d) >= 7:
        return d
    return []
cnt = 0
num = 400_000_001
while cnt != 5:
    if f(num):
        print(f(num)[6], len(f(num)))
        cnt += 1
    num += 1

