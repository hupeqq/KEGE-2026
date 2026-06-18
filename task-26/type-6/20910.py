with open('../files/26_20910.txt') as file:
    n, m, k = map(int, file.readline().split())
    seats = [10 ** 10] * (k + 1)
    for i in file:
        seat, row = map(int, file.readline().split())
        seats[row] = min(seats[row], seat) - 1
ans_row = 0
ans_seat = 0
for i in range(len(seats) - 1):
    if min(seats[i], seats[i + 1]) > ans_seat:
        ans_row = min(seats[i], seats[i + 1])
        ans_seat = i
print(ans_row, ans_seat)
