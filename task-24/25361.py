from re import finditer
with open('./files/24_25361 (1).txt') as file:
    data = file.readline()
pattern = '[02468]([^02468F]*[F]){76}[^02468F]*'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))