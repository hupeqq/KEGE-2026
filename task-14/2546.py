num = hex(4**38 + 3*4**20 + 4**15 + 2*4**7 + 49)[2:]
res = ''
cnt =0
for i in str(num):
    if i not in res:
        res += str(i)
        cnt += 1
    else:
        continue
print(cnt)