# while True 에서 '대박' 출력 1초휴식
# 메인에서 사건 10회출력 1초 휴식
# 메인이 끝나면 쓰레드도 종료


import threading, time

class ThreadEx1(threading.Thread):
    def run(self) -> None :
        i = 0
        while True:
            i += 1
            print('대박', i)
            time.sleep(1)

th = ThreadEx1()
th.daemon = True
th.start()

for j in range(10):
    print("사건 ", j)
    time.sleep(1)

