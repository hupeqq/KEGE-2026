from re import finditer
with open('./files/24_12254.txt') as file:
    data = file.readline()
pattern = 'S?Q?(RSQ)+R?S?'
res = [i.group() for i in finditer(pattern, data)]
print(len((max(res, key=len))))
