import threading, time

class Thread1(threading.Thread):
    def run(self) -> None: # 매소드에 리턴값이 없다는 의미
        # for i in range(100):
        i = 0
        while True:
            i += i
            print('i = {} '.format(i))
            time.sleep(1)

th = Thread1()

# main 이 끝나면 모든 쓰레드 종료
th.daemon = True # 반드시 start 전에 설정
th.start()

for j in range(10):
    print('j = {}'.format(j))
    time.sleep(1)