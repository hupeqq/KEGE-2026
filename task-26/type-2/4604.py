with open('../files/26_4604.txt') as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]
boxes = sorted(boxes)[::-1]
biggest = boxes[0]
ans = [biggest]
for i in range(1, len(boxes)):
    if biggest - boxes[i] >= 3:
        ans += [boxes[i]]
        biggest = boxes[i]
minim = 0
if ans[-1] > boxes[-1]:
    minim = boxes[-1]
print(len(ans), minim)