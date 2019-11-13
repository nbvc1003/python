
# 1~45 사이즈이 숫자중에 랜덤으로 6개의 숫자

from random import *

def gener_lotto():
    number = []
    while len(number) < 6 :
        # 1~45 사이의 랜덤 정수
        ran = randint(1,45)
        # not in  : number 라는 데이터집합에 ran값이 없다면
        if ran not in number:
            number.append(ran)
    #작은숫자부터 정렬
    return sorted(number)

print(gener_lotto())


# 임의의 숫자 값 입력후 나머지 랜덤
def gener_lotto_opt():
    number = []
    #임의의 번호를 사용자가 고정 하도록 수정
    print("몇개 :")
    num = int(input())

    while len(number) < num:
        print("숫자입력 ")
        inputnum = int(input())
        if inputnum not in number:
            number.append(inputnum)

    while len(number) < 6 :
        # 1~45 사이의 랜덤 정수
        ran = randint(1,45)
        # not in  : number 라는 데이터집합에 ran값이 없다면
        if ran not in number:
            number.append(ran)
    #작은숫자부터 정렬
    return sorted(number)


print(gener_lotto_opt())



