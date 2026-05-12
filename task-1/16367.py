from itertools import permutations
graph = 'EF FD DC CA AG GB BE AB FC'.split()
matrix = '246 16 57 15 347 127 356'.split()
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)