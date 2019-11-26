#threading .Thread를 상속받아서
# run 대박 10회 1초슬립, self.getName()사용하여출력

import threading, time

class ThreadEx(threading.Thread):
    # run 매소드에 재정의해서 사용 
    def run(self):
        for i in range(10):
            # self.getName() 각 쓰레드를 구분하는 목적으로 사용 생성자에서 지정가능
            print('대박 : {} -- {}'.format(self.getName(), i))
            time.sleep(1)


for k in range(2):
    th = ThreadEx()
    th.start()

