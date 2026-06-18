from re import finditer

with open('../files/24_17878.txt') as file:
    data = file.readline()
num = '([1-9][0-9]*|0)'
pattern = fr'({num}[-*])+{num}'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))