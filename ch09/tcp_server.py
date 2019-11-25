from socket import *
# AF_INET : ipv4, SOCK_STREAM : tcp방식
svrsock = socket(AF_INET, SOCK_STREAM)
HOST = '192.168.1.148'# 현재 pc주소 localhost, 127.0.0.1
PORT = 7001
svrsock.bind((HOST, PORT)) # ip주소와 포트 주소 ..


# 한번에 연결할수 있는 갯수 ..xx개로 셋
svrsock.listen(20)
#클라이언트가 연결할때 까지 대기
conn, addr = svrsock.accept()

# 클라이언트 ip주소
print("addr:", addr)
conn.send("hello >>".encode())

while True:
    # 클라이언트가 보내는 데이터를 1024byte씩 읽는다.
    b = conn.recv(1024)
    revMsg = b.decode()
    print(revMsg)
    #메시지를 다시 보내기
    conn.send(revMsg.encode())


#연결끊기
# conn.close()
