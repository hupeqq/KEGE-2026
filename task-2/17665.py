from itertools import product, permutations
def f(w, x, y, z):
    return (z <= (not(y <= x))) or w
for i in product((0, 1), repeat=7):
    table = [
        (i[0], 1, i[1], i[2]),
        (i[3], i[4], 0, 0),
        (i[5], 0, 1, i[6])
    ]
    if len(table) == len(set(table)):
        for p in permutations('wzxy'):
            if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
                print(''.join(p))