with open('files/24_8510.txt') as file:
    data = file.readline()
data = data.replace('N','*')
data = data.replace('O','*')
data = data.replace('P','*')
while '**' in data:
    data = data.replace('**', '* *')
data = data.split()
print(len(max(data, key=len)))
