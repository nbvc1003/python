import time


def Thread1(id):
    for i in range(10):
        print('id={} = {}'.format(id, i))
        time.sleep(1) # 1초 슬립

# 일반적인 순차 실행 예
for j in range(2):
    Thread1('{}번 쓰레드'.format(j))
print("메인 종료")



        