with open('./files/1_17.txt') as file:
    data = [int(i) for i in file]
mini = min(i for i in data if i > 0 and i % 123 == 0)
ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 + num2 < mini:
        ans.append(num1 + num2)
print(len(ans), abs(max(ans)))
#### 5001 962