from math import dist
def edge(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return max(res)[1]
with open('./files/27.17.A_19566.txt') as file:
    dots = [list(map(float, i.split())) for i in file]
eps = 1
clusters1 = []
while dots:
    cluster1 = [dots.pop()]
    for dot in cluster1:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster1.append(d)
                dots.remove(d)
    if len(cluster1) > 5:
        clusters1.append(cluster1)
edges = [edge(cluster) for cluster in clusters1]
print(sum(edge[0] for edge in edges) * 5000)
print(sum(edge[1] for edge in edges) * 5000)
with open('./files/27.17.B_19566.txt') as file:
    dots = [list(map(float, i.split())) for i in file]
eps = 0.7
clusters2 = []
while dots:
    cluster2 = [dots.pop()]
    for dot in cluster2:
        for d in dots.copy():
            if dist(dot, d) < eps:
                cluster2.append(d)
                dots.remove(d)
    if len(cluster2) > 4:
        clusters2.append(cluster2)
edges2 = [edge(cluster) for cluster in clusters2]
print(sum(edge[0] for edge in edges2) * 2500)
print(sum(edge[1] for edge in edges2) * 2500)