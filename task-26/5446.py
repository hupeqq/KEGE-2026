with open('files/26_5446.txt') as file:
    n = int(file.readline())
    pipes = []
    for i in file:
        pipes.append(list(map(int, i.split())))
pipes = sorted(pipes, key=lambda x: (-x[0] + x[1] * 2))
print(pipes)
big = pipes[0]
ans = [big[0]]
for pipe in pipes:
    if big[0] - big[1] * 2 - pipe[0] >= 3:
        ans.append(pipe[0])
        big = pipe
print(len(ans), ans[-1], ans)