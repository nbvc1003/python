
while True:
    li = [1,2,3]
    print('인덱스 번호를 입력하세요')
    num1 = input()
    if num1 == 'x':
        break
    try:
        num = int(num1)
        print('{} / 2 = {}'.format(li[num], li[num]/2))

    # 각 예외별로 처리 할경우
    # except IndexError:
    #     print("exception 인덱스 값이 범위 밖입니다.")
    # except ValueError:
    #     print("exception 입력된 값이 숫자가 아닙니다 ")

    # 예외상황 자체를 받아서 처리 할때
    except Exception as err:
        # as 의 역활 전달된 객체을 받아온다?
        print("에러 : {} ".format(err))

    # Exception이 발생하지 않았을때 처리
    else:
        print("예외상황이 없을경우 처리")
    finally:
        print("예외 여부와 상관없이 무조건 실행")
    



