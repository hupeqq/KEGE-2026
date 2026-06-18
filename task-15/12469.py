from itertools import combinations
def f(x):
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    a = a1 <= x <= a2
    return d <= ((not c and not a) <= (not d))
ans = []
line_a = [7, 29, 68, 100]
line_x = [8, 30, 70]
for a1, a2 in combinations(line_a, 2):
    if all(f(x) for x in line_x):
        ans.append(a2 - a1)
print(min(ans))
