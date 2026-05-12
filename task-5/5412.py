cnt = 0
ans = []
for n in range(1, 100000):
    r = hex(n)[2:]
    if r.count('b') % 2 == 0:
        r = '1' + r
    else:
        r += '1'
    res = int(r, 16)
    if len(str(res)) == 2:
        ans.append(n)
print(len(ans))