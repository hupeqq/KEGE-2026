with open('../files/24_2942.txt') as file:
    data = file.readline()
l = 0
cnt = 0
ans = 0
while l < len(data):
    if data[l:l+2] in 'AB AC':
        cnt += 1
        l += 2
    else:
        ans = max(ans, cnt)
        cnt = 0
        l += 1
print(ans)
