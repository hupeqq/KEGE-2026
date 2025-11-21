num = 729**8 - 3**18 + 85
res = ''
while num:
    res += str(num % 9)
    num //= 9
print(res.count('0'))