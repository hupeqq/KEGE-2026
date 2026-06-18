with open('./files/17_17558.txt') as file:
    data = [int(i) for i in file]
triz_dva = sum(1 for i in data if abs(i) % 32 == 0)
ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = num1 < 0
    u2 = num2 < 0
    if u1 + u2 >= 1:
        if num1 + num2 < triz_dva:
            ans.append(num1 + num2)
print(len(ans), max(ans))