with open('26_4629.txt') as file:
    N = int(file.readline())
    costs = []
    for i in file:
        costs.append(int(i))
costs.sort(reverse=True)
sale = N // 4
sale_prod = costs[:sale]
other_prod = costs[sale:]
cnt1 = 0
for i in sale_prod:
    cnt1 += i / 2
cnt2 = 0
for i in other_prod:
    cnt2 += i

cnt = cnt1 + cnt2
print(cnt)

costs.sort()
sale = N // 4
sale_prod = costs[:sale]
other_prod = costs[sale:]
cnt1 = 0
for i in sale_prod:
    cnt1 += i / 2
cnt2 = 0
for i in other_prod:
    cnt2 += i

cnt = cnt1 + cnt2
print(cnt)

print(sum(costs[N - sale:]) / 2 + sum(costs[:N - sale]))
print(sum(costs[:sale]) / 2 + sum(costs[sale:]))




