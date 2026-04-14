num = input()
ps = ""
for i in range(-1, len(num) * (-1) - 1, -1):
    ps += str(num[i])
print(ps)


