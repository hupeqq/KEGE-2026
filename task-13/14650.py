from ipaddress import *
for m in range(10, 31):
    net1 = ip_network(f'216.54.187.235/{m}', 0)
    net2 = ip_network(f'216.54.174.128/{m}', 0)
    if ip_address('216.54.187.235') in net1.hosts() and ip_address('216.54.174.128') in net2.hosts():
        if net1 != net2:
            print(m)
