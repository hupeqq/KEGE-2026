with open('../files/26_4660 (1).txt') as file:
    n = int(file.readline())
    costs = [int(i) for i in file]
costs = sorted(costs)
ans2 = sum(costs) - sum(costs[:n // 4]) // 2
ans1 = 0
res = 0
for i in range(0, len(costs), 4):
    res += costs[i] // 2
ans1 = sum(costs) - res
costs = costs[::-1]
ost = n % 4
if ost != 0:
    ans1 += sum(costs[:ost])
print(ans1, ans2)
