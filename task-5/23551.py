for n in range(1, 100000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '10'
    else:
        r = '1' + r + '01'
    if int(r, 2) < 30:
        print(n)