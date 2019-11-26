import threading, time

shareData = []

cv = threading.Condition()
class Produce(threading.Thread):
    def run(self):
        global shareData
        for i in range(10):
            cv.acquire() # 생산시 lock을 걸어준다.
            print('공유자원 생산')
            shareData.append(i)
            time.sleep(1)
            cv.notify() # 생산 종료 공지
            cv.release() # lock 풀어줌..


class Customer(threading.Thread):
    def run(self) -> None:
        global shareData
        for i in range(10):
            cv.acquire() # lock
            if len(shareData) < 1:
                cv.wait() # 작업을 하지 않고 기다린다. notify만나면 다시 시작
            print('공유자원 사용')
            print(shareData.pop())
            time.sleep(1)
            cv.release() # release

pro = Produce()
cus = Customer()
pro.start()
cus.start()

