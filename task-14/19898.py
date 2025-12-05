ans = []
for x in range(1, 10001):
    num = 7**270 + 7**170 + 7**70 - x
    cnt = 0
    for i in str(num):
        if num % 7 == 0:
            cnt += 1
    ans.append(cnt)
print(max(ans))