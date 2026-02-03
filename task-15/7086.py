def f(a, x):
    b = 50 <= x <= 70
    f = (x % a == 0) or (b <= (x % 16 != 0))
    return f
for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)