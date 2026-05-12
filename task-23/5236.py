def f(s, e, cnt=0):
    cnt += 1
    if s == e and cnt > 52:
        return 1
    if s > e:
        return 0
    return f(s + 2, e, cnt) + f(s * 4, e, cnt) + f(s * 3, e, cnt)
print(f(2, 400, 0))