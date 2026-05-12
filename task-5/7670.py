ans = []
for n in range(151, 100000):
    rt = hex(n)[2:]
    r = rt.replace('a', '1')
    cnt = 0
    for i in r:
        if i in '02468ace':
            cnt += 1
    if cnt > 2:
        r += 'b'
    else:
        r = 'f' + r
    res = int(r, 16)
    ans.append([res, n])
print(min(ans))
