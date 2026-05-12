from math import dist
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
with open('./files/1_27_B.txt') as file:
    dots = []
    orange_gigs = []
    yellow_dwarfs = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'K' and data[2:] == 'III':
            orange_gigs.append(list(map(float, [x, y])))
        elif data[0] == 'G' and data[2:] == 'V':
            yellow_dwarfs.append(list(map(float, [x, y])))
cluster1 = [[d for d in dots if d[1] < 30]]
cluster2 = [d for d in dots if d[1] > 30 and d[0] < 16]
cluster3 = [d for d in dots if d[1] > 30 and d[0] > 16]

cluster1 = [[d for d in dots if d[1] < 30],
            [dot for dot in orange_gigs if dot in cluster1]]
cluster2 = [[d for d in dots if d[1] > 30 and d[0] < 16],
            [dot for dot in orange_gigs if dot in cluster2]]
cluster3 = [[d for d in dots if d[1] > 30 and d[0] > 16],
            [dot for dot in orange_gigs if dot in cluster3]]
clusters = sorted(list([cluster1, cluster2, cluster3]), key=lambda x: (-len(x[1])))
print(dist(center(clusters[1][0]), center(clusters[2][0])) * 10000)
yell1 = [d for d in yellow_dwarfs if d in cluster1[0]]
yell2 = [d for d in yellow_dwarfs if d in cluster2[0]]
yell3 = [d for d in yellow_dwarfs if d in cluster3[0]]
max1 = 0
max2 = 0
max3 = 0
for d in yell1:
    for dot in yell1:
        max1 = max(dist(dot, d), max1)
for d in yell2:
    for dot in yell2:
        max2 = max(dist(dot, d), max2)
for d in yell3:
    for dot in yell3:
        max3 = max(dist(dot, d), max3)
print(max((max1, max2, max3)) * 10000)
##### 138716 34029