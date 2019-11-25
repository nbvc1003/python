from socket import *

HOST = 'localhost'# 현재 pc주소 localhost
PORT = 8001

sock = socket(AF_INET, SOCK_DGRAM)
while True:
    print(" 보낼 메시지를 입력하세요")
    msg = input()
    sock.sendto(msg.encode(), (HOST, PORT))
    s, addr = sock.recvfrom(1024)

    print(s.decode())
    print(addr)

