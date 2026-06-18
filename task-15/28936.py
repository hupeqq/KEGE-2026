def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = (x * y < a) or (5 * x < y) or (486 <= x)
            if not f:
                return False
    return True
for a in range(1, 50000):
    if f(a):
        print(a)
        break