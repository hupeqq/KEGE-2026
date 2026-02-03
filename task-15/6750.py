def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x + y <= 32) or (y <= x + 4) or (y >= a)
            if not f:
                return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)