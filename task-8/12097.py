from itertools import product
p = product('АГДИЛНРЯ', repeat=6)
cnt = 0
for i in p:
    s = ''.join(i)
    cnt += 1
    if cnt % 2 == 0 and s[0] != 'Я' and s.count('Д') == 3:
        print(cnt, s)