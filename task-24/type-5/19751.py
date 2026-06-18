from re import finditer
with open('../files/24_19751.txt') as file:
    data = file.readline()
num = '[1-9]+'
pattern = fr'(?<=A)({num}\+)+{num}|(?<=A){num}'
res = [i.group() for i in finditer(pattern, data)]
ans = 0
for i in res:
    ans = max(ans, eval(i))
print(ans)