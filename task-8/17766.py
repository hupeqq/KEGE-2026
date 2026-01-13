from itertools import product
alph = sorted('СЕНТЯБРЬ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    if pos % 2 == 0 and val.count('Ь') == 0 and val[0] == 'Р':
        print(val, pos)