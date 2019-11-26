
import threading, time


def prn(n):
    #대박이라고 n번 쓰레드 10회 출력하고 1초씩 sleep
    for i in range(10):
        print('{} 번쓰레드 대박:{} \n'.format(n,i))
        time.sleep(1)


# thread를 사용하여 prn 실행 n에 1,2 사용
# 사건 이라는 글자를 10회 실행


for i in range(1, 3):
    id = '대박 {} '.format(i)
    th = threading.Thread(target=prn, args=(id,))
    th.start()

for k in range(10):
    print("메인 사건",k)
    time.sleep(1)
