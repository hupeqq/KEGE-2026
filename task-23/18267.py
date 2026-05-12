def f(s, e):
    if s == e:
        return 1
    elif s ** 2 == e:
        return f(s + 2, e) + f(s + 5, e)
    elif s > e:
        return 0
    elif s < e:
        return f(s + 2, e) + f(s + 5, e) + f(s ** 2, e)
print(f(4, 36))