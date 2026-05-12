def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0 and prime(i):
            d |= {i}
        if num % (num // i) == 0 and prime(num // i) and num // i != num:
            d |= {num // i}
    d = sorted(list(d))
    if len(d) >= 4:
        m = d[0] + d[1] + d[-1] + d[-2]
        if m % 114 == 39:
            return m
    return 0
num = 456790
cnt = 0
while cnt != 5:
    res = f(num)
    if res:
        print(num, res)
        cnt += 1
    num += 1
