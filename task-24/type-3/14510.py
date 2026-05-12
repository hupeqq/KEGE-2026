from string import ascii_uppercase
with open('../files/24_14510.txt') as file:
    data = file.readline()
for i in ascii_uppercase:
    if i in 'AEIOYU':
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '#')
data = data.split('##*')
ans = 10**10
for i in range(len(data) - 500):
    if i in [0, len(data) - 500]:
        ans = min(ans, len('YAY'.join(data[i:i + 499])) + 3)
    else:
        ans = min(ans, len('YAY'.join(data[i:i + 499])) + 6)
print(ans)