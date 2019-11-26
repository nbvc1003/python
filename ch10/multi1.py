import threading, time

g_count = 0 # 모든 쓰레드에서 공유
class Thread1(threading.Thread):
    def run(self):
        global g_count # 전역 변수로 선언
        for i in range(10):
            
            print('id = {}증가전 -- >{}'.format(self.getName(), g_count))
            g_count += 1
            time.sleep(1)
            print('id = {}증가후 -- >{}'.format(self.getName(), g_count))

for i in range(2):
    th = Thread1()
    th.start()


