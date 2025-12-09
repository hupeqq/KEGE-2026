from itertools import product
alph = sorted('ЯНВАРЬ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != 'Я' and 'ЯЯ' not in val and val.count('Ь') <= 1:
        print(pos)