with open('26_17565 (1).txt') as file:
    N, S = map(int, file.readline().split())
    sailors = []
    for i in file:
        a1, a2, a3, a4, a5 = map(int, i.split())
        sailors.append([a2 + a3 + a4, a5, a1])
sailors.sort(key=lambda x: (-x[0], -x[1], -x[2]))
print(sailors[:S])
print(sailors[S:S+15])