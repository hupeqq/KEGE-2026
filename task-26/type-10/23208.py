with open(r'..\files\26_23208.txt') as file:
    N = int(file.readline())
    pieces = []
    for pos, data in enumerate(file, start=1):
        time_1, time_2 = map(int, data.split())
        if min(time_1, time_2) == time_1:
            pieces.append([time_1, 's', pos])
        else:
            pieces.append([time_2, 'o', pos])
pieces = sorted(pieces)
last_piece = pieces[-1]
cnt = sum(1 for piece in pieces if piece[1] == 's')
print(last_piece[2], cnt - 1 if last_piece[1] == 's' else cnt)