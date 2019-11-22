def some():
    print("1부터 10사이의 숫자를 입력하세요")
    num = int(input())
    if num < 1 or num > 10:
        raise Exception('유효하지 않습니다.{}'.format(num))
    else:
        print("입력한 숫자는 {}입니다.".format(num))

# 함수를 처리할때 외부에서 에러 처리가 가능하다.
try:
    some()
except Exception as err:
    # 함수 내부에서 발생한 Exeption을 받아서 최종 처리한다.
    print("대박 에러네 > {}".format(err))


