ans = []
for x in range(1, 2031):
    res = ''
    num = 7**170 + 7**100 - x
    while num:
        res += str(num % 7)
        num //= 7
    ans.append([x, res.count('0')])
print(max(ans))

