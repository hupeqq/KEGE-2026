with open('../files/26_21910.txt') as file:
    n = int(file.readline())
    boxes = [int(i) for i in file]
boxes = sorted(boxes)[::-1]
biggest = boxes[0]
ans = [biggest]
for box in boxes:
    if biggest - box >= 9:
        ans.append(box)
        biggest = box
print(len(ans), ans[-1])