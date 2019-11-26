import time, threading

# 쓰레드의 갯수를 제한 한다.
sema = threading.Semaphore(3)

class Thread1(threading.Thread):
    def run(self) -> None:
        sema.acquire()
        time.sleep(1)
        print(self.getName())
        sema.release()

for i in range(10):
    th = Thread1()
    th.start()
