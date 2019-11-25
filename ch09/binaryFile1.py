
# 바이너리 형식으로 쓸때 wb
f = open('bin.txt', 'wb')
f.write('안녕 컴동지들'.encode())
f.close()

# 바이너리 형식을 읽을때 rb
f = open('bin.txt', 'rb')
dat = f.read()
print(dat.decode())
# print(dat)
f.close()