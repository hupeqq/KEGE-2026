def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for n in range(1, 100000):
    r = convert(n, 3)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += convert(sum(map(int, str(n))), 3)
    res1 = int(r, 3)
    if res1 % 2 == 0 and res1 > 220:
        print(res1)
        break