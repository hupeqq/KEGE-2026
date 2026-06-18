from re import finditer
with open('./files/8835.txt') as file:
    data = file.readline()
pattern = r'([^M\.]*M){112}[^M\.]*\.'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))

