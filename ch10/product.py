import time, threading


shareData = []

class Producer(threading.Thread):
    def run(self):
        global shareData
        for i in range(10):
            print('공유 자원 생산')
            time.sleep(1)
            shareData.append(i)

class Customer(threading.Thread):
    def run(self):
        global  shareData
        for i in range(10):
            print('공유자원 소비')
            time.sleep(1)
            print(shareData.pop())


pro = Producer()
cus = Customer()

pro.start()
cus.start()




