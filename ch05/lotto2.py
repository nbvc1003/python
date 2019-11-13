
from random import *

# set 을 사용하여 단순하게 작성된 로또 번호 생성함수
def lotto_num():
    nums = set()
    while len(nums) < 6:
        nums.add(randint(1,45))

    return sorted(nums)

print(lotto_num())

def lotto_num2():
    nums = set()

    #inputNum = int( if isnuberics(input("갯수 입력")))
    inputNum = int(input(  "갯수 입력") )
    while len(nums) < inputNum:
        nums.add(int(input("숫자 입력 :")))

    while len(nums) < 6:
        nums.add(randint(1,45))

    return sorted(nums)

print(lotto_num2())