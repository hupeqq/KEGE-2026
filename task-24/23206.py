from re import finditer
with open('./files/24_23206.txt') as file:
    data = file.readline()
pattern = '[02468]([^02468S]*[S]){35}[^02468S]*'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))