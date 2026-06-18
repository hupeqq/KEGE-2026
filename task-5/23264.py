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
        r += r[-2:]
    else:
        r += conv((n % 3) * 5, 3)
    res = int(r, 3)
    if res > 150:
        ans.append(res)
print(min(ans))