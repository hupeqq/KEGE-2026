def f(x, y, s):
    if x + y >= 77: return s % 2 == 0
    if s == 0: return 0
    h = [f(x + 3, y, s - 1), f(x, y + 3, s - 1), f(x, y * 3, s - 1), f(x * 3, y, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)
print(*[y for y in range(1, 65) if f(12, y, 2)])
print(*[y for y in range(1, 65) if f(12, y, 3) and not f(12, y, 1)])
print(*[y for y in range(1, 65) if f(12, y, 4) and not f(12, y, 2)])