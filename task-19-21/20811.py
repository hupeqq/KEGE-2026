def f(x, s):
    if x >= 51: return s % 2 == 0
    if s == 0: return 0
    h = [f(x + 1, s - 1), f(x + 4, s - 1), f(x * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)
print(*[x for x in range(1, 51) if f(x, 2)])
print(*[x for x in range(1, 51) if f(x, 3) and not f(x, 1)])
print(min([x for x in range(1, 51) if f(x, 4) and not f(x, 2)]))