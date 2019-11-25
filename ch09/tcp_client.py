from socket import *
sock = socket(AF_INET, SOCK_STREAM)

HOST = '192.168.1.148'
# HOST = '192.168.1.180'
PORT = 7001

sock.connect((HOST, PORT))

while True:
    b = sock.recv(1024)
    print(b.decode())

    print("전달할 말을 입력하세요")
    msg = input()
    sock.send(msg.encode())




#sock.close()