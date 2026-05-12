with open(r'./files/26_4629.txt') as file:
    n = int(file.readline())
    costs = sorted([int(i) for i in file])
cons = sum(costs) - sum(costs[-n//4:]) // 2
shop = sum(costs) - sum(costs[:n//4]) // 2
print(cons, shop)

