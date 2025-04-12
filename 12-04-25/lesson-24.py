with open('26_954.txt') as file:
    N, K, M = map(int, file.readline().split())
    prices = []
    for i in file:
        prices.append(int(i))
prices.sort(reverse=True)
most_exp = prices[:K]
most_exp1 = prices[K:K+M]
sale = 0
for i in most_exp:
    sale += i * 0.2
for i in most_exp1:
    sale += i * 0.1
maxim = prices[K+M]
print(maxim, sale)

