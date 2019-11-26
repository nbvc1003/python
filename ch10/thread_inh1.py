import threading, time

# 클래스를 상속 받는 방식으로 쓰레드 구현
class ThreadEx1(threading.Thread):
    # thread를 상속 받은 경우에는 run method 재정의
    def run(self):
        for i in range(10):
            # self.getName() 실행하는 쓰레드 순서값을 가져온다.
            print('id = {} ----> {} '.format(self.getName(), i))
            time.sleep(1)
            
for i in range(2):
    th = ThreadEx1()
    th.start()
    
print("메인 종료")

