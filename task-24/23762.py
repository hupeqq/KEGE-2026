with open('./files/24_23762.txt') as file:
    data = file.readline()
data = data.split('Y')
ans = 0
for i in range(len(data) - 81):
    if 'Y'.join(data[i:i + 81]).count('2025') >= 90:
        ans = max(ans, len('Y'.join(data[i:i + 81])))
print(ans)