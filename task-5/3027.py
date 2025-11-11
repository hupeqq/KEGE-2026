cnt = 0
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += bin(r.count('1'))[2:]
    else:
        r = '1' + r + '00'
    if 500 <= int(r, 2) <= 700:
        cnt += 1
print(cnt)