with open('../files/26_4684 (1).txt') as file:
    n = int(file.readline())
    costs = [int(i) for i in file]
costs = sorted(costs, reverse=True)
ost = n % 6
extra = sum(costs[:ost])
costs = sorted(costs)
ans2 = sum(costs) - sum(costs[:n // 6]) // 2
ans1 = 0
for i in range(ost, len(costs), 6):
    ans1 += costs[i] // 2
ans1 = sum(costs) - ans1
print(ans1, ans2)