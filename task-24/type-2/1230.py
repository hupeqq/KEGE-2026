from re import finditer
with open('../files/24_1230.txt') as file:
    data = file.readline()
pattern = '[^WRQ]+'
print(len(max([i.group() for i in finditer(pattern, data)], key=len)))