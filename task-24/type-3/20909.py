with open('../files/24_20909.txt') as file:
    data = file.readline()
ans = 0
data = data.split('AB')
for i in range(len(data) - 100):
    if i in [0, len(data) - 100]:
        ans = max(ans, len('AB'.join(data[i:i + 101])) + 1)
    else:
        ans = max(ans, len('AB'.join(data[i:i + 101])) + 2)
print(ans)
