def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if prime(i): d|={i}
            if prime(num // i): d|= {num // i}
    if len(d) == 3:
        return max(d)
    return 0
numb = 1000001
cnt = 0
while cnt != 5:
    res = f(numb)
    if res:
        print(numb, res)
        cnt += 1
    numb += 1