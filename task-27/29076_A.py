from math import dist
with open('./files/27_A_29075.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] == '2':
            stars.append(list(map(float, [x, y])))
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
svet1 = [dot for dot in stars if dot in cluster1]
svet2 = [dot for dot in stars if dot in cluster2]
if len(svet1) < len(svet2):
    print(center(cluster1)[0] * 10000)
    print(center(cluster2)[1] * 10000)