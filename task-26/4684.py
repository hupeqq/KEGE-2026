with open(r'./files/26_4660.txt') as file:
    n = int(file.readline())
    costs = sorted([int(i) for i in file])
ans2 = sum(costs) - sum(costs[:n//6]) // 2
res = 0
ost = len(costs) % 6
for cost in range(ost, len(costs), 6):
    res += costs[cost]
ans1 = sum(costs) - res // 2
print(ans1, ans2)