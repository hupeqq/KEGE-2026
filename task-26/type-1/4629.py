with open('../files/26_4629 (1).txt') as file:
    n = int(file.readline())
    costs = [int(i) for i in file]
costs = sorted(costs)
ans1 = sum(costs) - sum(costs[:n // 4]) // 2
costs = sorted(costs, reverse=True)
ans2 = sum(costs) - sum(costs[:n // 4]) // 2
print(ans2, ans1)