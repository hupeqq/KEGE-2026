from itertools import product
p = product('ДЖОС', repeat=6)
cnt = 0
for i in p:
    s = ''.join(i)
    cnt += 1
    if s[0] == 'Ж' and s[1] == 'С':
        print(cnt)
