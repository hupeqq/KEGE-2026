cnt = 0
for p in range(0, 16):
    for k in range(0, 16):
        for b in range(0, 16):
            if k > p > b and k + p + b <= 15:
                cnt += 1
print(cnt)