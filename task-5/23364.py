def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = conv(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r += conv(4 * (n % 3), 3)
    res = int(r, 3)
    if res < 100:
        ans.append([n, res])
print(max(ans))

