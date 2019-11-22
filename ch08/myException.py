class MyException(Exception):
    def __init__(self, arg):
        super().__init__("정수가 아니다 : {}".format(arg))


def convert(num):
    if num.isdigit():
        return int(num)
    else:
        raise MyException(num)



try:
    print("숫자를 입력하세요 :")
    num = input()
    a = convert(num)

except MyException as err:
    print("에러네 : {} ".format(err))
else:
    print("입력한 수 {} 타입 {}".format(a, type(a)))

