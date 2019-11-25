

from socket import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 8002))
msg, addr = sock.recvfrom(1024)
print(msg.decode())
print(addr)
sock.close()