from timeit import timeit


def Tim1():
    with open("26_2944.txt") as file:
        s, n = map(int, file.readline().split())
        size = [int(i) for i in file]
    size.sort()
    cnt_size = []
    for i in size:
        cnt_size.append(i)
        if sum(cnt_size) > s:
            cnt_size.pop()
            break
    size.sort(reverse=True)
    for i in size:
        if sum(cnt_size) - cnt_size[-1] + i <= s:
            cnt_size = cnt_size[:-1]
            cnt_size.append(i)
            break


def Tim2():
    with open("26_2944.txt") as file:
        s, n = map(int, file.readline().split())
        size = [int(i) for i in file]
    size.sort()

    cnt_size = []
    for i in size:
        if i <= s:
            s -= i
            cnt_size.append(i)

    size.sort(reverse=True)
    s += cnt_size.pop()
    for i in size:
        if i <= s:
            cnt_size.append(i)
            break

def Rom1():
    with open('26_2944.txt') as file:
        S, N = map(int, file.readline().split())
        size = [int(i) for i in file]
    size.sort()

    cnt_users = 0
    size_users = 0
    last_user = 0
    for i in size:
        if size_users + i <= S:
            cnt_users += 1
            size_users += i
            last_user = i
        else:
            break

    S = S - size_users
    max_user = 0
    for i in size[::-1]:
        if i <= S + last_user:
            max_user = i
            break

def Rom2():
    with open('26_2944.txt') as file:
        S, N = map(int, file.readline().split())
        size = [int(i) for i in file]
    size.sort()

    cnt_users = 0
    last_user = 0
    for i in size:
        if i <= S:
            S -= i
            cnt_users += 1
            last_user = i
        else:
            break

    max_user = 0
    for i in size[::-1]:
        if i <= S + last_user:
            max_user = i
            break

time1 = timeit(Tim1, number=1000)
time2 = timeit(Tim2, number=1000)
time3 = timeit(Rom1, number=1000)
time4 = timeit(Rom2, number=1000)

print(time1)
print(time2)
print(time3)
print(time4)