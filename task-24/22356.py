from idlelib.pyshell import restart_line
from re import *
with open('./files/24_22356.txt') as file:
    data = file.readline()
pattern = '[1-9AB][0-9AB]*[13579B]'
res = [i.group() for i in finditer(pattern, data)]
print(data.index(max(res, key=lambda x: (len(x), int(x, 12)))))
