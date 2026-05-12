from math import dist
with open('./files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] >= '8':
            stars.append(list(map(float, [x, y])))
stars1 = [d for d in stars if d[1] > 23]
stars2 = [d for d in stars if d[1] < 23 and d[1] > 15]
stars3 = [d for d in stars if d[1] < 15]

dists1 = []
for s1 in stars1:
    for s2 in stars2:
        dists1.append(dist(s1, s2))
for s2 in stars2:
    for s3 in stars3:
        dists1.append(dist(s2, s3))
for s1 in stars1:
    for s3 in stars3:
        dists1.append(dist(s1, s3))
dists2 = []
for s1 in stars1:
    for s2 in stars1:
        if s1 != s2:
            dists2.append(dist(s1, s2))
for s1 in stars2:
    for s2 in stars2:
        if s1 != s2:
            dists2.append(dist(s1, s2))
for s1 in stars3:
    for s2 in stars3:
        if s1 != s2:
            dists2.append(dist(s1, s2))
print(sum(dists2) / len(dists2) * 10000)