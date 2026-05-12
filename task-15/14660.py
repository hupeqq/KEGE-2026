from itertools import combinations
def f(x):
    p = 16 <= x <= 84
    q = 27 <= x <= 43
    a = a1 <= x <= a2
    return (a <= p) or q
ans = []
line_a = [16, 27, 43, 84]
line_x = [17, 28, 44]
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(max(ans))