with open(r'./files/17_21595.txt') as file:
    data = [int(i) for i in file]
ans = []
square = len([i for i in data if str(i)[-1] == '3' and 1000 <= abs(i) <= 9999]) ** 2
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if max(num1, num2, num3) + (num1 + num2 + num3 - max(num1, num2, num3) - min(num1, num2, num3)) > square:
        ans.append(num1 + num2 + num3)
print(len(ans), abs(max(ans)))