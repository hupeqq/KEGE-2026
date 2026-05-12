ans = []
for delit in range(113, 1_000_000, 226):
    for i in range(1, 13):
        num = delit + 3 ** i
        if num in range(100000, 1000000) and str(num).count('0') == 0:
            ans.append([num, i])
for i in sorted(ans)[:5]:
    print(*i)
