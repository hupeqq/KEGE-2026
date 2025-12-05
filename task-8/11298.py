from itertools import product
p = product('АЖЗОПЮ', repeat=6)
cnt0 = 0
cnt1 = 0
for i in p:
    s = ''.join(i)
    cnt0 += 1
    if cnt0 % 2 == 0 and s[0] == 'А' and s.count('З') >= 2:
        cnt1 += 1
print(cnt1)
