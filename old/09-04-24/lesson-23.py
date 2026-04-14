with open('26_21424.txt') as file:
    n = int(file.readline())
    lengths = []
    for i in file:
        lengths.append(int(i))
lengths.sort(reverse=True)
last = []
next = float('inf')
for i in lengths:
    if next - i >= 9:
        last.append(i)
        next = i
print(len(last), last[-1])