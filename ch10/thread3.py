import threading, time

def sum(low, high):
    tot = 0
    for i in range(low, high):
        tot += i
        time.sleep(0.01)

    print("합계 {}".format(tot))

# target : 함수, args : 매게변수
t = threading.Thread(target=sum, args=(1, 100))
t.start()

