def f(s, cnt=0):
    if cnt == 14:
        return {s}
    return f(s + 10, cnt + 1) | f(s - 5, cnt + 1)
print(len(f(1)))