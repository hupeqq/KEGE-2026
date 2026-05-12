from itertools import combinations


def f(x):
    b = 23 <= x <= 37
    c = 41 <= x <= 73
    a = a1 <= x <= a2
    return ((not b) <= c) <= a
line_a = [23, 37, 41, 73]
line_x = [24, 38, 42]
ans = []
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))