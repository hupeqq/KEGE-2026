from itertools import combinations
def f(x):
    b = 22 <= x <= 40
    c = 32 <= x <= 50
    a = a1 <= x <= a2
    return (not a) <= (b == c)
list_a = [22, 32, 40, 50]
list_x = [23, 33, 41]
ans = []
for a1, a2 in combinations(list_a, 2):
    if all(f(x) for x in list_x):
        ans.append(a2 - a1)
print(min(ans))
##### 28