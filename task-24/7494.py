with open('files/7494.txt') as file:
    data = file.readline()
data = data.split('DE')
ans = ''
for i in range(len(data) - 240):
    ans = max(ans, 'E' + 'DE'.join(data[i:i + 241]) + 'D', key=len)
print(len(ans))