def f(a):
    for x in range(1, 10000000):
        f = ((405 % x == 0) <= (81 % x == 0)) or (a - x > 162)
        if not f:
            return False
    return True
for a in range(1, 10000000):
    if f(a):
        print(a)
        break