with open('./files/24_29354 (1).txt') as file:
    data = file.readline()
data = data.split('BC')
ans = 0
for i in range(len(data) - 190):
    ans = max(ans, len('BC'.join(data[i:i + 191])) + 2)
print(ans)