with open(r'./files/26_589.txt') as file:
    n = int(file.readline())
    prices = [int(i) for i in file]
prices = sorted(prices)
disc = 0
for i in range(len(prices) - 1):
    if (prices[i + 1]) // 500 != (prices[i] +1 ) // 500:
        print(prices[i + 1], prices[i])
print(disc)
