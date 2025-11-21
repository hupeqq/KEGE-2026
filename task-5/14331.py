def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
nums = []
for n in range(1, 100000):
    r = convert(n, 3)
    if (r.count('1') + r.count('2') * 2) % 3 == 0:
        r += '212'
    else:
        r += convert((r.count('1') + r.count('2') * 2) * 2, 3)
    result = int(r, 3)
    if result > 490:
        nums.append(result)
print(min(nums))
