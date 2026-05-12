from itertools import permutations

graph = 'AH HF FE ED DG GA FB BC BH CG'.split()
matrix = '478 38 256 15 34 37 168 127'.split()

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
