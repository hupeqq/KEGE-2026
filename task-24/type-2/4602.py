with open('../files/24_4602.txt') as file:
    data = file.readline()
data = data.replace('A', 'O')
for i in 'BC':
    data = data.replace(i, 'D')
data = data.replace('DO', '*')
for i in 'DO':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
###################################

with open('../files/24_4602.txt') as file:
    data = file.readline()
ans = 0
for i in range(len(data) - 1):
    if data[i] in 'BCD' and data[i + 1] in 'AO':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j] in 'BCD' and data[j + 1] in 'AO':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
#########################
from re import finditer
with open('../files/24_4602.txt') as file:
    data = file.readline()
pattern = '([BCD][AO])+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)) / 2)
###################################
with open('../files/24_4602.txt') as file:
    data = file.readline()
l = 0
cnt = 0
ans = 0
while l < len(data):
    if data[l] in 'BCD' and data[l + 1] in 'AO':
        cnt += 1
        l += 2
    else:
        ans = max(ans, cnt)
        cnt = 0
        l += 1
print(ans)