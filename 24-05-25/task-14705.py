def reading_data():
    with open("26_14705.txt") as file:
        n = int(file.readline())
        exp = [list(map(int, i.split())) for i in file]
    return exp


def making_timeline():
    exp = reading_data()
    timeline = [0] * 5_000_000
    for i in exp:
        timeline[i[0]] += 1
        timeline[i[1]] -= 1
    return timeline


def finding_answers():
    timeline = making_timeline()
    prefix_timeline = [0] * 5_000_000
    prefix_timeline[0] = timeline[0]
    cnt = 0
    ans = 0
    for i in range(1, 5000000):
        prefix_timeline[i] = timeline[i] + prefix_timeline[i - 1]
    max_cnt = max(prefix_timeline)
    for i in prefix_timeline:
        if i == max_cnt:
            cnt += 1
            ans = max(cnt, ans)
        else:
            cnt = 0
    return max(prefix_timeline), ans


print(finding_answers())
