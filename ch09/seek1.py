import os

# wb+ 이진파일 읽고 쓰기   : + 가 뒤에 붙을 경우 파일을 읽고 나서 다른 작업을 한다는 의미
f = open('t.txt','wb+')
# b로 시작하는 것은 데이터가 binary라는의미
s = b'01234567890123456789'
f.write(s)
f.seek(5)

# tell 현재위치 반환
print('현재 위치 : {}'.format(f.tell()))
print('읽은 값 : {}'.format(f.read(1)))

# 내장함수에서 정의된 상수값
# SEEK_SET = 0 #
# SEEK_CUR = 1 # 현재위치기준
# SEEK_END = 2 #마지막 기준
f.seek(-3, os.SEEK_END) # 마지막 위치에서 앞쪽 방향으로 3 칸
print('읽은 값 : {}'.format(f.read(1)))


f.close()