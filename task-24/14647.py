with open('./files/24.14_14647.txt') as file:
    data = file.readline()
indexes = []
l = 0
ans = 0
for i in range(len(data)):
    if data[i] in 'XY':
        indexes.append(i)
        if len(indexes) > 2:
            l = indexes[0] + 1
            indexes.remove(indexes[0])
    if len(indexes) == 2 and data[indexes[0]] != data[indexes[1]]:
        ans = max(ans, i - l + 1)
print(ans)