def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (x < 7) or (y >= 5*x + a - 60) or (x >= 36) or (y < 225)
            if not f:
                return False
    return True
for a in range(0, 1000):
    if f(a):
        print(a)