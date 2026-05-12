from ipaddress import ip_network
net = ip_network('172.140.68.0/255.255.248.0', 0)
cnt = 0
for ip in net:
    if f'{int(ip):032b}'.count("0") > 15:
        cnt += 1
print(cnt)