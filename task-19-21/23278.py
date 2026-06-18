def f(x, s):
    if x <= 16: return s %2  == 0
    if s == 0: return 0
    h = [f(x - 3, s - 1), f(x - 8, s - 1), f(x // 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)
print([x for x in range(17, 500) if f(x, 2)])
print([x for x in range(17, 500) if f(x, 3) and not f(x, 1)])
print([x for x in range(17, 500) if f(x, 4) and not f(x, 2)])