def f(x):
    d = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return d
for num in range(int(106732567 ** .5), int(152673837 ** .5)):
    if len(f(num ** 2)) == 3:
        print(num ** 2, max(f(num ** 2)))
