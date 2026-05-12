with open('../files/24_1975.txt') as file:
    data = file.readline()
data = data.replace('PP', 'P P')
print(len(max(data.split(), key=len)))
######
ans = 0
cnt = 1
with open('../files/24_1975.txt') as file:
    data = file.readline()
for i in range(len(data) - 1):
    if data[i] + data[i + 1] != 'PP':
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1
print(ans)
###########
from re import finditer
pattern = r'(?=P)P(([^P]+[P])+)[^P]+P(?<=P)'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))