from re import finditer
from string import printable

with open('../files/24_21421.txt') as f:
    data = f.readline()
pattern = '[1-9AB][0-9AB]*[02468A]'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))
############
with open('../files/24_21421.txt') as f:
    data = f.readline().lower()
ans = 0

for i in printable[12:]:
    data = data.replace(i, ' ')
data = data.split()
for line in data:
    line = line.lstrip('0').rstrip('13579b')
    ans = max(len(line), ans)
print(ans)