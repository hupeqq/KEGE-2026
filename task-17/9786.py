with open(r'files\17_9786.txt') as file:
    data = [int(i) for i in file]
ans = []
maxi = max(i for i in data if abs(i) % 100 == 25)
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if sum((999 < abs(i) <= 9999) for i in (num1, num2, num3)) < 3:
        if num1 + num2 + num3 <= maxi:
            ans.append(num1 + num2 + num3)
print(len(ans), max(ans))
