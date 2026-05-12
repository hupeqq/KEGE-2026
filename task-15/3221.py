def f(a):
    for x in range(1, 1000):
        n = ((x % 3 == 0) <= (x % 5 != 0)) or (x + a >= 70)
        if not n:
            return False
    return True
for a in range(1, 1000):
    if f(a):
        print(a)
        break