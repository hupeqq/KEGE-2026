def f(a):
    for x in range(0, 1000):
        b = 70 <= x <= 90
        f = (x % a == 0) or (b <= (not x % 22 == 0))
        if not f:
            return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)