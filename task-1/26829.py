from itertools import permutations
graph = 'ВД ДГ ГБ БЖ ЖЕ ЕВ ДА АЕ АК КГ КБ'.split()
matrix = '248 137 268 15 467 357 256 13'.split()
for i in permutations('АБВГЕДЖК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
