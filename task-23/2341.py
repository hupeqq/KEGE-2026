def f(s, h=0):
    if h == 8:
        if s in range(1000, 1025): return {s}
        return set()
    return f(s + 1, h + 1) | f(s + 5, h + 1) | f(s * 3, h + 1)
print(len(f(1)))
