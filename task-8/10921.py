from itertools import permutations
alph = 'ДЖАВАСКРИПТ'
cnt = 0
for val in set(permutations(alph, len(alph))):
    val = ''.join(val)
    if val.index('И') + val.find('А') + val.rfind('А') == 8:
        cnt += 1
print(cnt)
