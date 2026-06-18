with open('./files/24_17535.txt') as file:
    data = file.readline()
data = data.split('CD')
ans = 0
for i in range(len(data) - 160):
    ans = max(ans, len('D' + 'CD'.join(data[i:i + 161]) + 'C'))
print(ans)