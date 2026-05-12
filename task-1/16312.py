from itertools import permutations
graph = 'AC CD AD AG GD DB DE EF FB'.split()
matrix = '37 57 147 37 26 57 12346'.split()

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)