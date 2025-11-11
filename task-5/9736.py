nums = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin((n % 3) * 3)[2:]
    if int(r, 2) <= 170:
        nums.append(int(r, 2))
print(max(nums))