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
        if num % i == 0 and prime(i) and i % 10 == 7:
            d |= {i}
        if num % (num // i) == 0 and prime(num // i) and num // i != num and (num // i) % 10 == 7:
            d |= {num // i}
    d = sorted(list(d))
    if len(d) >= 1:
        f = sum(d) // len(d)
        if f % 111 == 0:
            return f
    return 0
num = 749999
cnt = 0
while cnt != 5:
    res = f(num)
    if res:
        print(num, res)
        cnt += 1
    num -= 1