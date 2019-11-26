import time, threading


def Thread1(id):
    for i in range(10):
        print('id={} = {}'.format(id, i))
        time.sleep(1) # 1초 슬립

# 일반적인 순차 실행 예
for j in range(2):
    id = '{}번 쓰레드'.format(j)
    # target 실행할 메소드명 , args 전달할 데이터 (tuple)
    th = threading.Thread(target=Thread1, args=(id,))
    # 쓰레드의 실행
    th.start()
print("메인 종료")