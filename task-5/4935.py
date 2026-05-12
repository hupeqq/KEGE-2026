ans = []
for n in range(1, 100000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[:-2] + '00'
    else:
        r = '11' + r[:-2] + '11'
    res = int(r, 2)
    if n < 30:
        ans.append([res, n])
print(ans)
