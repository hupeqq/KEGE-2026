a = []
for n in range(4, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += r[:3]
    else:
        r = '1' + r + '01'
    if int(r, 2) > 600:
        a.append(int(r, 2))
print(min(a))