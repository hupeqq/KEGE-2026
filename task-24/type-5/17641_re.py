from re import finditer
with open('../files/24_17641.txt') as file:
    data = file.readline()
num = r'([1-9][0-9]*|0)'
prod = rf'({num}\*)*0(\*{num})*'
pattern = fr'({prod}\+)+{prod}'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))