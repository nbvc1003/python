import socket

# tcp 상호 연결된 상태에서 작동
# udp 
# 각 프로토콜의 포트 번호 리턴
print(socket.getservbyname('http','tcp'))
print(socket.getservbyname('ftp','tcp'))


