from math import dist
with open('./files/27_A_29079.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[2:] == 'IV' and data[0] == 'N':
            stars.append(list(map(float, [x, y])))
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]
cluster1 = [d for d in dots if d[1] > 8]
cluster2 = [d for d in dots if d[1] < 8]
oran1 = [d for d in stars if d in cluster1]
oran2 = [d for d in stars if d in cluster2]
dists1 = []
for d in oran1:
    dists1.append(dist(d, center(cluster2)))
dists2 = []
for d in oran2:
    dists2.append(dist(d, center(cluster1)))
print(min(min(dists1), min(dists2)) * 10000)
print(max(max(dists1), max(dists2)) * 10000)