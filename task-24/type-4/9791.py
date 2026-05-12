from string import printable

with open('../files/24_9791.txt') as file:
    data = file.readline().lower()
cnt = 0
ans = 0
for i in data:
    if i == '0' and cnt == 0:
        continue
    if i in printable[:16]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 0
ans = max(cnt, ans)
print(ans)