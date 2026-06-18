with open('./files/9004.txt') as file:
    data = file.readline()
data = data.split('Z')
ans = 'y'* 10**10
for i in range(len(data) - 268):
    ans = min(ans, 'Z' + 'Z'.join(data[i:i + 269]) + 'Z', key=len)
print(len(ans))