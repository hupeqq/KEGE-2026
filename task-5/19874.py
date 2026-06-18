def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = conv(n, 3)
    if n % 4 == 0:
        r += r[-3:]
    else:
        r = '1' + r + '20'
    res = int(r, 3)
    if res > 423:
        ans.append(res)
print(min(ans))