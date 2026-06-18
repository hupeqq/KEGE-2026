from fnmatch import fnmatch
for num in range(161, 10**8 + 1, 161):
    if fnmatch(str(num), '12*4?65'):
        print(num, num // 161)
