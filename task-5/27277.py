def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = conv(n, 3)
    if n % 3 != 0:
        r = '1' + r + r[-3:]
    else:
        r += conv(sum(map(int, r)) * 8, 3)
    res = int(r, 3)
    ans.append(res)
mini = 100000
for num in ans:
    mini = min(abs(1220 - num), mini)
for i in ans:
    if abs(1220 - i) == mini:
        print(i)