def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 50):
    for y in range(1, 50):
        num = conv(5 ** 50 + 5 ** 30 - 5 ** x - y - 5 ** y - x, 5)
        if int(num, 5) > 0 and num.count('0') == 10:
            print(x * y)
            break