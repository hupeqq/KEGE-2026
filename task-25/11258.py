from fnmatch import fnmatch
for x in range(8387, 10**9, 8387):
    if fnmatch(str(x), '*75?122*'):
        print(x, x // 8387)