def f(a):
    for x in range(1, 1000):
        f = (x % 21 == 0) <= ((not x % a == 0) <= (not x % 77 == 0))
        if not f:
            return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)