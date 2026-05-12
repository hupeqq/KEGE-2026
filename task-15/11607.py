def f(a):
    for x in range(1, 50000):
        f = not((x % 263 == 0) <= (x % a == 0)) and (x % 71 == 0)
        if f:
            return False
    return True
for a in range(25000, 1, -1):
    if f(a):
        print(a)
        break