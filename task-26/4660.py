with open(r'./files/26_4660.txt') as file:
    n = int(file.readline())
    costs = sorted([int(i) for i in file])
ans2 = sum(costs) - sum(costs[:n//4]) // 2
res = 0
for cost in range(0, len(costs), 4):
    res += costs[cost]
ans1 = sum(costs) - res // 2
costs = sorted(costs, reverse=True)
ost = len(costs) % 4
if ost != 0:
    ans1 += sum(costs[:ost])
print(ans1, ans2)