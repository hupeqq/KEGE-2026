for n in range(2, 10000000):
    r = bin(n)[2:]
    cnt_0 = r[::2].count('0')
    cnt_1 = r[1::2].count('1')
    res = abs(cnt_1 - cnt_0)
    if res == 5:
        print(n)
        break