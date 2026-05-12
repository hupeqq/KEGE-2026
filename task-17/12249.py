with open('files/17_12249.txt') as file:
    data = [int(i) for i in file]
ans = []
mini = max(i for i in data if abs(i) % 10 == 3 and 9999 < i <= 99999)
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = abs(num1) % 10 == 3
    u2 = abs(num2) % 10 == 3
    u3 = abs(num3) % 10 == 3
    if u1 + u2 + u3 >= 1:
        if num1 + num2 + num3 <= mini:
            ans.append(num1 + num2 + num3)
print(len(ans), max(ans), mini)