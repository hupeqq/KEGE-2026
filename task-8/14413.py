from itertools import permutations
cnt = 0
alph = 'СОРТИРОВКА'
for val in set(permutations(alph, 10)):
    val = ''.join(val)
    for i in val:
        if i in 'ИАО':
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '#')
    if '***' not in val and '###' not in val:
        cnt +=1
print(cnt)