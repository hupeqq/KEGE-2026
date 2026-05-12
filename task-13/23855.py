from ipaddress import ip_network
net = ip_network('172.95.116.174/255.255.192.0', 0)
for ip in net.hosts():
    print(sum(map(int, str(ip).split('.'))))
    break