data = input()
data = data.split(".")
data = " ".join(data)
data = data.split(",")
data = " ".join(data)
data = data.split()
ans = 0
word = ""
for i in data:
    cnt = len(i)
    if cnt > ans:
        ans = cnt
        word = i
print(ans, word)
