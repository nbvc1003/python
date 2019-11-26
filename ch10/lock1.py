import threading, time

g_count = 0

class Thread1(threading.Thread):
    def run(self):
        global g_count
        for i in range(10):
            lock.acquire() # 내가 사용하는 동아 접근 금지 
            print('id {} 증가전 --> {}'.format(self.getName(), g_count))
            g_count += 1
            time.sleep(1)
            print('id {} 증가후 --> {}'.format(self.getName(), g_count))
            lock.release() # 다른쓰레드에서 사용하도록 해지

lock = threading.Lock()
for j in range(2):
    th = Thread1()
    th.start()