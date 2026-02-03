from fnmatch import fnmatch
for x in range(154682, 10**11 + 1, 154682):
    if fnmatch(str(x), '*192?3*68'):
        print(x, x // 154682)