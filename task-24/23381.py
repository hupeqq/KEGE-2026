with open('./files/24_23381.txt') as file:
    data = file.readline()
ans = 0
cnt = 0
for i in '2468':
    data = data.replace(i, '0')
for i in '3579':
    data = data.replace(i, '1')
for i in range(len(data) - 1):
    if data[i] == '0':
        cnt += 1
