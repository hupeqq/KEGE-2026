with open(r'./files/26_17687.txt') as file:
    n = int(file.readline())
    prices = [int(i) for i in file]
prices = sorted(prices, reverse=True)
k = 9
price_cust = sum(prices) - sum(prices[:n // k])
price_shop = sum(prices) - sum(prices[k - 1::k])
print(price_cust, price_shop)