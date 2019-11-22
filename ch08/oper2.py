

# li [1,2,3,4,5]인덱스를 입력받아서 *2 해서 출력
# x를 입력하면 종료
# exception 처리
# 정상일때 수고
# 에러 여부에 상관없이 밥먹고 하자

li = [1,2,3,4,5]
while True:
    try:
        ip = input("숫자를 입력하세요")
        if ip == 'x':
            break

        num = int(ip)
        print("{} * 2 ={}".format(li[num], li[num]* 2))
        
    except ValueError as err:
        print(err)
    except IndexError as err:
        print(err)
    else:
        print("수고")




