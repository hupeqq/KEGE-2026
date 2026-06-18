from itertools import permutations

graph = 'AG GE EB BD CD CF FA FG BC'.split()
matrix = '24 134 267 125 47 37 356'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
