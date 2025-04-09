with open('26_17687.txt') as file:
    N = int(file.readline())
    costs = []
    for i in file:
        costs.append(int(i))
sale = N // 9
costs.sort()
print(sum(costs[:N - sale]))
print(sum(costs[sale:]))
