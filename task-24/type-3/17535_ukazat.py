with open('../files/24_17535.txt') as file:
    data = file.readline()
ans = cnt = r = l = 0
len_data = len(data)
while r < len(data) - 1:
    if cnt <= 1:
        if data[r] + data[r + 1] == 'CD': cnt += 1
        r += 1
    else:
        if data[l] + data[l + 1] == 'CD': cnt -= 1
        l += 1
    ans = max(ans, r - l)
print(ans)