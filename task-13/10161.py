from ipaddress import *
ip1 = ip_address('211.115.61.154')
ip2 = ip_address('211.115.59.137')
for mask in range(16, 25):
    net = ip_network(f'{ip1}/{mask}', 0)
    if ip1 in net and ip2 in net:
        print(net.netmask)
