with open('../files/26_17881.txt') as file:
    n = int(file.readline())
    students = [list(map(int, i.split())) for i in file]
students = sorted(students, key=lambda x: (-(x[1] + x[2] + x[3] + x[4]) / 4, x[0]))
passed = []
not_passed = []
for i in students:
    if 2 not in i[1:]:
        passed.append(i[0])
    else:
        not_passed.append([i[0], i[1:].count(2)])
print(passed[:n // 4][-1])
for i in not_passed:
    if i[1] == 3:
        print(i[0])
        break
