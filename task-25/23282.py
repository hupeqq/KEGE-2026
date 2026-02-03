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
            if prime(i): d.add(i)
            if prime(num // i): d.add(num // i)
    if len(d) > 1:
        m = min(d) + max(d)
        if m > 60000 and str(m) == str(m)[::-1]:
            return m
    return 0
num = 5_400_001
cnt = 0
while cnt != 5:
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1
