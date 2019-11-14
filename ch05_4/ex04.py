

pin = "881120-1068234"


def isMan(num):
    # 1이면 2000년 이전 출생남자
    # 2이면 2000년 이전 출생한 여자
    # 3이면 2000년 이후 출생한 남자
    # 4이면 2000년 이후 출생한 여자
    # 5이면 외국인 남자
    # 6이면 외국인 여자
    # 7이면


        if num[8] == 1:
            print('2000년 이전 출생남자')
        elif num[8] == 2:
            print('2000년 이전 출생여자')
        elif num[8] == 3:
            print('2000년 이후 출생남자')
        elif num[8] == 4:
            print('2000년 이후 출생여자')
        elif num[8] == 5:
            print('외국인 남자')
        elif num[8] == 6:
            print('외국인 여자 ')
        else:
            print('기타')



isMan("761003-1618016")


# replace 함수 사용
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)
b = [1,3,5,4,2]
b.sort()
print(b)
b.reverse()
print(b)

a = ['life','is','too','short']
result = ' '.join(a)
print(result)


