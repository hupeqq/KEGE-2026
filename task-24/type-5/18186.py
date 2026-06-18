from re import finditer
with open('../files/24_18186.txt') as file:
    data = file.readline()
g = r'[AE]'
s = r'[BCDHGF]'
pattern = rf'(?<={s}{s}{g}).+?(?={s + s + g})'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)) + 6)
