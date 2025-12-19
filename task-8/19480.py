from itertools import permutations
cnt = 0
alph = 'ПАРИЖАНКА'
for val in set(permutations(alph, 9)):
    val = ''.join(val)
    for i in val:
        if i in 'ИА':
            val = val.replace(i, '*')
    if val.count('**') == 1 and val.count('***') == 0:
        cnt+= 1
print(cnt)