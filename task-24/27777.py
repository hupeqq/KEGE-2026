from re import finditer
with open('./files/24_27777.txt') as file:
    data = file.readline()
pattern = f'[1-9AB][0-9AB]*'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))