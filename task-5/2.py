def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    res = res[::-1]
    return res

for n in range(1, 100000):
    r = str(conv(n, 4))
    if n % 4 == 0:
        r = '2' + r + '03'
    else:
        r += str(conv((n % 4) * 5, 4))
    result = int(r, 4)
    if result < 567:
        print(n)

