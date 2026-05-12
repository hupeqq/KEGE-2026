def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
for x in range(1, 2301):
    num = 7**350 + 7**150 - x
    if convert(num, 7).count('0') == 200:
        print(x)