from itertools import permutations
graph = 'АБ БВ ВД БД ДК ДЕ ВЕ ВГ ГЕ ЕК'.split()
matrix = '27 1567 67 5 246 2357 1236'.split()
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)