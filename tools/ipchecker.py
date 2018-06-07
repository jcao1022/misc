import IPy

from IPy import IP

print(IP('192.168.0.1').version())
print(IP('::1').version())

ip = IP('192.168.0.0/16')
# print(ip.len())
# for i in ip:
#     print(i)
print(ip.iptype())
ip.reverseName()
ip.int()
ip.strHex()
ip.strBin()
ip.net()
ip.netmask()

print(IP('192.168.0.0').make_net('255.255.255.0'))
print(IP('192.168.0.0-192.168.0.255', make_net=True))






























