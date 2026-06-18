with open('./files/24_27634.txt') as file:
    data = file.readline()
data = data.split('Z')
ans = 10**10
for i in range(1, len(data) - 271):
    ans = min(ans, len('Y'.join(data[i:i + 269])) + 2)
print(ans)