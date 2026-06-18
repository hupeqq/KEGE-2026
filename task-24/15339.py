from re import finditer
with open('./files/24_15339.txt') as file:
    data = file.readline()
pattern = '[6-9]([ABC][6-9])+[ABC]'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))