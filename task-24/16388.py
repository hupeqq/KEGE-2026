from re import finditer
with open('./files/24_16388.txt') as file:
    data = file.readline()
pattern = '(LMN|MN|N)*(KLMN)+(KLM|KL|K)*'
res = [i.group() for i in finditer(pattern, data)]
print(len(max(res, key=len)))
########################################
with open('./files/24_16388.txt') as file:
    data = file.readline()
data = data.replace('KLMN', '****')
data = data.replace('LMN*', ' ****')
data = data.replace('MN*', ' ***')
data = data.replace('N*', ' **')
data = data.replace('*KLM', '**** ')
data = data.replace('*KL', '*** ')
data = data.replace('*K', '** ')
for i in 'KLMN':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))