from itertools import permutations
print(*range(1, 9))
graph = 'DE DB BE EA BG HG HC CF GF'.split()
matrix = '38 58 146 36 27 347 568 127'.split()
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)