a = []
def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(11, 100000):
    r = convert(n, 3)
    cnt_0 = 0
    cnt_1 = 0
    for i in r:
        if i in '02468':
            cnt_0 += 1
        else:
            cnt_1 += 1
    if cnt_0 > cnt_1:
        r = '22' + r
    else:
        r = '11' + r
    if int(r, 3) > 100:
        a.append(int(r, 3))
print(min(a))