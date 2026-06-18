with open('../files/26_2_23175.txt') as file:
    n, m = map(int, (file.readline().split()))
    info = [int(i) for i in file]
cargos = sorted(info[:n])
conts = sorted(info[n:])
ans = []
last_cont = 0
for cargo in cargos:
    for cont in conts:
        if cont >= cargo:
            ans.append(cargo)
            last_cont = cont
            conts.remove(last_cont)
            break
ans = ans[:-1]
for i in cargos[::-1]:
    if last_cont -i >= 0:
        ans.append(i)
        break
print(len(ans), ans[-1] - ans[-2])
