def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True
def f(num):
    d = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if prime(i) and str(i).count('5') == 1: d += [i]
            if prime(num // i) and str(num // i).count('5') == 1: d += [num // i]
    if len(d) == 2 and d[0] * d[1] == num:
        return max(d)
    return 0
num = 1324728
cnt = 0
while cnt != 5:
    if f(num):
        print(num, f(num))
        cnt += 1
    num += 1


