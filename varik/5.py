ans = []
for n in range(1, 100000):
    r = f'{n:b}'
    if sum(map(int, r)) % 2 == 0:
        r = '10' + r[2:] + '0'
    else:
        r = '11' + r[2:] + '1'
    res = int(r, 2)
    if res <= 19:
        ans.append(n)
print(max(ans))
###### 12