from itertools import permutations
cnt = 0
alph = 'росомаха'
for val in set(permutations(alph, 8)):
    val = ''.join(val)
    for i in val:
        if i in 'оа':
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '#')
    if '**' not in val and '##' not in val:
        cnt += 1
print(cnt)