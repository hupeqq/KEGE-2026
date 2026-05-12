with open('./files/26_17565.txt') as file:
    N, S = map(int, file.readline().split())
    sailors = []
    for i in file:
        id, e1, e2, e3, s = map(int, i.split())
        sailors.append([e1+e2+e3, s, id])
sailors = sorted(sailors, key=lambda x: (-x[0], -x[1], x[2]))
passed = sailors[:S]
rejected = sailors[S:]
half_score = passed[-1][0]
print([i[2] for i in passed[::-1] if i[0] != half_score][0])
half_passed = [1 for i in passed if i[0] == half_score]
half_rej = [1 for i in rejected if i[0] == half_score]
print(sum(half_rej) + sum(half_passed))