def count_near_standing_pairs_1(data):
    data = data.replace("O", "A")
    data = data.replace("C", "B")
    data = data.replace("D", "B")

    while "AA" in data or "BB" in data or "AB" in data:
        data = data.replace("AA", "A A")
        data = data.replace("BB", "B B")
        data = data.replace("AB", "A B")

    data = data.split()

    cnt = 0
    ans = 0
    for i in data:
        if i == "BA":
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 0
    print(ans)
def count_near_standing_pairs_2(data):
    data = data.replace("O", "A")
    data = data.replace("C", "B")
    data = data.replace("D", "B")

    data = data.replace("BA", "*")

    cnt = 0
    ans = 0
    for i in data:
        if i == "*":
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 0
    print(ans)

def count_near_standing_pairs_3(data):
    data = data.replace("O", "A")
    data = data.replace("C", "B")
    data = data.replace("D", "B")

    data = data.replace("AA", " ")
    data = data.replace("BB", " ")
    data = data.replace("AB", "1")
    data = data.split()

    ans = 0
    for i in data:
        if len(i) > ans:
            ans = len(i)

count_near_standing_pairs_3(data)
count_near_standing_pairs_3(data)
count_near_standing_pairs_3(data)