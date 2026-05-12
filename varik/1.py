from itertools import permutations
graph = 'AB BV VG GE EK KD DB VD VE ED'.split()
matrix = '27 1567 67 5 246 2357 1236'.split()
for i in permutations('ABVGEKD'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
### 9