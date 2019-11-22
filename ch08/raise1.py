

try:
    print("숫자를 입력하세요")
    num = int(input())
    print("숫자 :", num)

    # 의도적 에외발생...
    raise Exception("에러야")

except Exception as err:
    print("애공 {}".format(err))
