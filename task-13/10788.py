import ipaddress
from ipaddress import *
for m in range(10, 31):
    net = ip_network(f'201.44.240.107/{m}', 0)
    if ip_address('201.44.240.33') in net.hosts() and bin(int(net.network_address))[2:].count('1') >= 5:
        print(m)