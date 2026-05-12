with open('files/17_2473.txt') as file:
    data = [int(i) for i in file]
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = abs(num1) % 7 == 0
    u2 = abs(num2) % 7 == 0
    u3 = abs(num1) % 10 == 3
    u4 = abs(num2) % 10 == 3
    if u1 + u2 >= 1 and u3 + u4 >= 1:
        ans.append(num1 + num2)
print(len(ans), min(ans))