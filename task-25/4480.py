def f(num):
    d = set()
    proiz = 1
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d |= {i, num // i}
    d = list(d)
    if len(d) > 10 and sum(d) % 2 == 1:
        for i in d:
            proiz *= i
        if proiz % 2 == 1:
            return len(d)
    return 0
num = 800001
cnt = 0
while cnt != 6:
    res = f(num)
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1


