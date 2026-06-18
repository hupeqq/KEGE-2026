with open('../files/26_20910.txt') as file:
    n, m, k = map(int, file.readline().split())
    seats = [10 ** 10] * (k + 1)
    for i in file:
        row, seat = map(int, file.readline().split())
        seats[seat] = min(seats[seat], row) - 1
ans_seat = 0
ans_row = 0
for i in range(len(seats) - 1):
    if min(seats[i], seats[i + 1]) > ans_seat:
        ans_row = min(seats[i], seats[i + 1])
        ans_seat = i
print(ans_row, ans_seat)