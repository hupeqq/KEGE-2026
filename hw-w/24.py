with open('24_9075.txt') as file:
    data = file.readline()
cnt = 0
ans = 0
for i in data:
    if i in '02468':
        data = data.replace(i, '*')
    if i in '13579':
        data = data.replace(i, '#')
