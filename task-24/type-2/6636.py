from re import finditer
with open('../files/24_6636.txt') as file:
    data = file.readline()
pattern = '([24][135])+'
print(len(max([match.group() for match in finditer(pattern, data)], key=len)) / 2)