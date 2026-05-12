def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for n in range(1, 100000):
    r = convert(n, 7)
    if r[-1] == '7':
        r.replace('3', "*")
        r.replace('1', '3')
        r.replace('*', '1')
        r = '21' + r
    else:
        r = '1' + r[1:] + '36'
    res = int(r, 7)
    if res < 744:
        ans.append([n, res])
print(sorted(ans))