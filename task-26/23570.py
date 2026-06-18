with open('./files/26_23570.txt') as file:
    n, k = map(int, file.readline().split())
    powers = []
    for i in range(n):
        powers.append(int(file.readline()))
    snow = []
    for i in range(k):
        power, cost = map(int, file.readline().split())
        snow.append([power, cost])
powers = sorted(powers)
snow = sorted(snow, key=lambda x:(x[1], x[0]))
able = []
for p in powers:
    for s in snow.copy():
        if s[0] >= p:
            able.append([s[1], s[0]])
            break
        else:
            snow.remove(s)
print(sum(i[0] for i in able), able[-1][1])