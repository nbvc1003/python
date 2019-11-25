from socket import *
svrsock = socket(AF_INET, SOCK_DGRAM)

svrsock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
# 192.168.1.0 ~ 255  port : 8002 대역에 보낸다.
svrsock.sendto("그만보내욧.!!!! 건.....!!!!!!".encode(), ('192.168.1.255', 8002))
print("전송완료..")