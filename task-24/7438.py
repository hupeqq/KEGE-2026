with open('./files/7438.txt') as file:
    data = file.readline()
data = data.split('D')
res = []
for i in range(len(data) - 100):
    res.append('D'.join(data[i:i + 101]))
res = sorted(res, key=len)[::-1]
ans = ''
for i in res:
    i = i.replace('SD', 'S D').replace('DS', 'SD')
    for j in '0123456789':
        i = i.replace(j, ' ')
    i = i.split()
    for k in i:
        ans = max(ans, k, key=len)
print(len(ans))