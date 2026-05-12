with open(r'./files/26_6759.txt') as file:
    n = int(file.readline())
    costs = sorted([int(i) for i in file])
ost = len(costs) % 3
free = 0
for cost in range(ost, len(costs), 3):
    free += costs[cost]
ans2 = sum(costs) - free
free2 = 0
costs = sorted(costs, reverse=True)
for cost in range(0, len(costs) // 3):
    free2 += costs[cost]
ans1 = sum(costs) - free2
print(ans1, ans2)

