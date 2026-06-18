with open('./files/24_28765.txt') as file:
    data = file.readline()
data = data.split('BC')
ans = 0
for i in range(len(data) - 180):
    ans = max(ans, len('BC'.join(data[i:i + 181])) + 2)
print(ans)