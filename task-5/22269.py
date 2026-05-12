ans = []
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 100000):
    r = convert(n, 5)
    if r[-1] == '0':
        r = r.replace('1', '*')
        r = r.replace('4', '1')
        r = r.replace('*', '4')
        r = '33' + r
    else:
        r = '3' + r[1:] + '42'
    res1 = int(r, 5)
    if res1 < 1922:
        ans.append([res1, n])
print(sorted(ans))