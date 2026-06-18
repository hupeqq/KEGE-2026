def f(s, e):
    if s < e or s == 8:
        return 0
    if s == e:
        return 1
    return f(s - 1, e) + f(s - 4, e) + f(s // 3, e)
print(f(19, 14) * f(14, 2))