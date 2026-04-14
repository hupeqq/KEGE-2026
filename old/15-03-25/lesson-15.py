data = "A2A1BA221A1B1A1"
data = data.replace("B", "A")
data = data.replace("2", "1")
data = data.replace("A1", "*")
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

data = "A2A1BA221A1B1A1"
data = data.replace("B", "A")
data = data.replace("2", "1")
data = data.replace("A1", "*")
data = data.replace("A", " ")
data = data.replace("1", " ")
data = data.split()
cnt = 0
ans = 0
for i in data:
    ans = max(len(i), ans)
print(ans)



