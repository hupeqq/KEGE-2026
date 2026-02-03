from itertools import product, permutations
def f(a, b, c):
    return (a <= b) and ((a and b) <= (not c))

table = [
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
]
if len(set(table)) == len(table):
    for p in permutations('abc'):
        if [f(**dict(zip(p, t))) for t in table] == [1, 0, 1, 1, 1, 0, 1, 0]:
            print(''.join(p))