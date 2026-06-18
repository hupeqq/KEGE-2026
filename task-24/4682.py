from re import finditer
with open('./files/24_4682.txt') as file:
    data = file.readline()
pattern = '([AE][BCD])+'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)) // 2)
