from itertools import permutations
cnt = 0
gl = 'ЕОИА'
sogl = 'ЛВС'
alph = 'ЛЕВИОСА'
for val in set(permutations(alph, 7)):
    val = ''.join(val)
    if val[0] not in gl and val[len(val)//2 + 1] not in sogl:
        cnt += 1
print(cnt)

