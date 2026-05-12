with open('./files/17_5758.txt') as file:
    data = [int(i) for i in file]
moda = max(data.count(num) for num in data)
cnt = 0
for num in data:
    if data.count(num) == moda:
        res = num
for num1 in range(len(data) - 1):
    for num2 in range(num1 + 1, len(data)):
        if (data[num1] < res < data[num2] or data[num1] > res > data[num2]) and abs(num2 - num1) % 2 == 1:
            cnt += 1
            max_raz = max(abs(res - data[num1]), abs(res - data[num2]))
print(cnt, max_raz)
