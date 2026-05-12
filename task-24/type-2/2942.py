with open('../files/24_2942.txt') as file:
    data = file.readline()
data = data.replace('AB', '**')
data = data.replace('AC', '**')
for i in 'ABC':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)) / 2)
####################################
with open('../files/24_2942.txt') as file:
    data = file.readline()
ans = 0
for i in range(len(data) - 1):
    if data[i:i + 2] in 'AB AC':
        cnt = 1
        for j in range(i + 2, len(data) - 1, 2):
            if data[j:j + 2] in 'AB AC':
                cnt += 1
            else:
                break
        ans = max(ans, cnt)
print(ans)
#################
from re import finditer
with open('../files/24_2942.txt') as file:
    data = file.readline()
pattern = '(A[BC])+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))