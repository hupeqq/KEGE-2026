from fnmatch import fnmatch
for num in range(141, 10**8 + 1, 141):
    if fnmatch(str(num), '1234*7'):
        print(num, num // 141)
