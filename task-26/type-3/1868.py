with open('../files/26_1868.txt') as file:
    n = int(file.readline())
    seats = [list(map(int, i.split())) for i in file][:-1]
seats = sorted(seats, key=lambda x: (-x[0], x[1]))
for i in range(len(seats) - 1):
    if seats[i][0] == seats[i + 1][0]:
        if seats[i + 1][1] - seats[i][1] == 3:
            row = seats[i][0]
            seat = seats[i][1] + 1
            print(row, seat)
            break