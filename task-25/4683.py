from fnmatch import fnmatch
for num in range(37, 10**8 + 1, 37):
    if fnmatch(str(num), '2*1234?6'):
        print(num, num // 37)
