for n in range(1, 16):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '10' + r[2:] + '1'
    else:
        r = '11' + r[2:] + '0'
    res = int(r, 2)
    print(res)