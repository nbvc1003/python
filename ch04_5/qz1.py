

import random
# 1~100 숫자중 랜덤한 숫자
ran = random.randint(1, 100)

cnt = 0

while True:
    print("1~100 사이 정수를 입력하세요")
    num = int(input())
    cnt += 1
    if num == ran: break
    elif num > ran: print("작은 수를 입력하세요")
    else : print("큰수를 입력하세요")

print("{}번에 정답 {} 를 맞췄습니다. ".format(cnt, num))
        