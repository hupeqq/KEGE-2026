from ipaddress import *
ip1 = ip_address('218.48.192.56')
ans = set()
for mask in range(16, 25):
    net = ip_network(f'218.48.192.0/{mask}', 0)
    if ip1 in net.hosts() and net.num_addresses - 2 >= 500 and str(net.network_address) == '218.48.192.0':
        ans.add(f'{int(ip):032b}'[16:25] for ip in net.hosts())
print(len(ans))