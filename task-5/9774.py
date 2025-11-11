def conv(num, sys):
    res = ''
    while num:
        res += str(num % 3)
        num //= 3
    return res[::-1]
for n in 11, 12:
    r = conv(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += str(conv((n % 3) * 5, 3))
    if int(r, 3) > 133:
        print(int(r, 3))
        break

