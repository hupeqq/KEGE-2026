with open('../files/26_21719.txt') as file:
    n = int(file.readline())
    students = [list(map(int, i.split())) for i in file]
students = sorted(students)
cnt = 1
ans = []
for i in range(len(students) - 1):
    if students[i][0] == students[i + 1][0]:
        if students[i][1] == students[i + 1][1]:
            continue
        if students[i + 1][1] - students[i][1] == 2:
            cnt += 1
        else:
            cnt = 1
    else:
        cnt = 1
    ans.append([cnt, students[i][0]])
ans = sorted(ans, key=lambda x: (x[0], -x[1]))
print(ans[-1])