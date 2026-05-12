from re import finditer
with open('../files/24_23206.txt') as file:
    data = file.readline()
pattern = '[02468]([^02468S]*[S]){35}[^02468S]*'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))
#########################################
with open('../files/24_23206.txt') as file:
    data = file.readline()
for i in '02468':
    data = data.replace(i, ' 0')
data = data.split()
ans = 0
for line in data:
    if line.count('S') == 35:
        ans = max(ans, len(line))
    elif line.count('S') > 35:
        while line.count('S') > 35:
            line = line[:-1]
        ans = max(ans, len(line))
print(ans)