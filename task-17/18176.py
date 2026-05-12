with open(r'./files/17_18176.txt') as file:
    data = [int(i) for i in file]
mini = min(i for i in data if i > 0 and str(i)[-1] == '4')
ans = []
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    if sum(sum(map(int, str(abs(i)))) for i in (num1, num2, num3)) == mini:
        ans.append(num1 + num2 + num3)
print(len(ans), max(ans))