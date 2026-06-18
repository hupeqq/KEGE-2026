with open('./files/24_21717.txt') as f:
    data = f.readline()
data = data.replace('RSQ', 'Rsq rsQ')
ans = 10**10
for i in range(len(data) - 128: