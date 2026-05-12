with open('../files/24_4627.txt') as file:
    data = file.readline()
data = data.replace('NPO', '*')
data = data.replace('PNO', '*')
for i in 'PNO':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))
################################
with open('../files/24_4627.txt') as file:
    data = file.readline()
ans = 0
for i in range(len(data) - 2):
    if data[i:i + 3] in 'NPO PNO':
        cnt = 1
        for j in range(i + 3, len(data) - 2, 3):
            if data[j:j + 3] in 'NPO PNO':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
#######################################
from re import finditer
with open('../files/24_4627.txt') as file:
    data = file.readline()
pattern = '(PNO|NPO)+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)) / 3)
#########################################
with open('../files/24_4627.txt') as file:
    data = file.readline()
l = 0
cnt = 0
ans = 0
while l < len(data):
    if data[l: l + 3] in 'NPO PNO':
        cnt += 1
        l += 3
    else:
        ans = max(ans, cnt)
        cnt = 0
        l += 1
print(ans)