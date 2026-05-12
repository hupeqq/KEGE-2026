from re import finditer
with open('files/24_21509.txt') as file:
    data = file.readline()
pattern = fr'([789]+[0789]*[\*-])+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))