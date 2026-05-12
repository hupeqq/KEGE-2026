from re import finditer
with open('./files/24_20968.txt') as file:
    data = file.readline()
pattern = r'([1-9][0-9]*[02468][\+*])+[1-9][0-9]*[02468]'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))