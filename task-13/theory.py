from ipaddress import *
ip = ip_address('172.26.128.0')
# все айпи адреса по заданному айпи и маске
net = ip_network('172.16.128.0/255.255.192.0')
# Двоичное представление ip-адреса с добавлением ведущих нулей до 32х позиций
bin_ip = f'{int(ip):032b}'
# Широковещательный адрес. Не может быть присвоен устройству
broadcast_ip = net.broadcast_address

# Адрес сети. Не может быть присвоен устройству
network_ip = net.network_address

# Хосты - ip-адреса, которые могут быть присвоены устройствам
hosts = net.hosts()

# Общее кол-во ip-адресов в сети с учетом зарезервированных
num_addresses = net.num_addresses
mask = net.netmask