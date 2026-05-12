from fnmatch import fnmatch
def f(x):
    d = set()
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            d |= {i, x // i}
    return d
for num in range(53, 10**7 + 1, 53):
    if fnmatch(str(num), '*2?2*') and len(f(num)) > 30 and str(num) == str(num)[::-1]:
        print(num, sum(f(num)))