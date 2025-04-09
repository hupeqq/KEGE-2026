data = "ababacbbaabaccac"
delete = "ac"
cnt = ""
for i in delete:
    data = data.replace(i, "")
print(data)
for i in delete:
    data = data.split(i)
    data = "".join(data)
print(data)