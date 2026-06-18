from ipaddress import ip_network
for x in (0, 128, 192, 224, 240, 248, 252, 254, 255):
    net = ip_network(f'172.16.168.0/255.255.255.{x}')
    cnt = 0
    for ip in net:
        if bin(int(ip))[2:].count('0') % 7 == 0:
            cnt += 1
    if cnt == 35:
        print(x)
        break