with open('files/26_4604.txt') as file:
    n = int(file.readline())
    boxes = list(map(int, file.readlines()))
boxes = sorted(boxes, reverse=True)
big = boxes[0]
ans = [big]
for box in boxes:
    if big - box >= 3:
        ans.append(box)
        big = box
minim = 0
for i in ans:
    if ans[-1] > boxes[-1]:
        minim = boxes[-1]
print(len(ans), minim)
