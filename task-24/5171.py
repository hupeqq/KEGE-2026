from re import finditer
with open('./files/24_5171.txt') as file:
    data = file.readline()
pattern = '(CA)+C?'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))