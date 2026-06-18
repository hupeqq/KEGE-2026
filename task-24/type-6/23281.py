with open('../files/24_23281.txt') as file:
    data = file.readline()
data = data.split('Y')
ans = 0
for i in range(len(data) - 80):
    ans = max(ans, len('Y'.join(data[i:i + 81])))
print(ans)