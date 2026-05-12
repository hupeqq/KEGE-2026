num = 3*17**777 + 15*17**250 - 6*17**100 + 2
ans = set()
cnt = 0
while num:
    ans.add(num % 17)
    num //= 17
for i in set(ans):
    if i % 2 == 0:
        cnt += 1
print(cnt)