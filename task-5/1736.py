ans = []
for n in range(1, 100):
    r = bin(n)[2:]
    r = r.replace('0', '00')
    r = r.replace('1', '11')
    res = int(r, 2)
    if res > 63:
        print(res)
        break

