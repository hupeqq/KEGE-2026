from string import printable

with open('../files/24_21908.txt') as file:
    data = file.readline()
ans = ''
for i in printable[14:]:
    data = data.replace(i, ' ')
data = data.split()
for line in data:
    line = line.lstrip('0').rstrip('13579bd')
    ans = max(line, ans, key=lambda x: (len(x), x))
print(len(ans))
############

from re import finditer
with open('../files/24_21908.txt') as file:
    data = file.readline()
pattern = '[1-9ABCD][0-9ABCD]*[2468AB0]'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=lambda x: (len(x), x))))