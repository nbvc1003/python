from socket import *

HOST = 'localhost'# 현재 pc주소 'localhost'
PORT = 8001
svrsock = socket(AF_INET, SOCK_DGRAM)

svrsock.bind((HOST, PORT))
print('서버 가동중')

while True:
    s, addr = svrsock.recvfrom(1024)
    print('IP:{} >'.format(addr), end="")
    print(s.decode())
    svrsock.sendto(s, addr)