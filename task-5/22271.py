def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = f(n, 8)
    if r[0] == '5':
        r = r.replace('1', '*')
        r = r.replace('2', '1')
        r = r.replace('*', '2')
        r = '11' + r
    else:
        r = '2' + r[1:] + '10'
    res = int(r, 8)
    if res < 1354:
        ans.append([res, n])
print(max(ans))