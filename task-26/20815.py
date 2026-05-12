with open('./files/26_20815.txt') as file:
    N, K = map(int, file.readline().split())
    astronauts = []
    for i in file:
        id, s1, s2, s3, s = map(int, i.split())
        astronauts.append([s1 + s2 + s3 + s, s, id])
astronauts = sorted(astronauts, key=lambda x: (-x[0], -x[1], x[2]))
passed = astronauts[:K]
rejected = astronauts[K:]
half_score = passed[-1][0]
last_passed = [i[2] for i in passed[::-1] if i[0] != half_score][0]
half_scored = sum(1 for i in astronauts if i[0] == half_score)
print(last_passed, half_scored)