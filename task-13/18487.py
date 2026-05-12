from ipaddress import ip_network
def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') > 15
cnt = 0
for a in range(0, 256):
    net = ip_network(f'192.214.{a}.184/255.255.255.224', 0)
    if all(f(ip) for ip in net):
        print(a)
        break