

#숫자를 입력받아서 2~9 이면 while문을 사용해서 구구단 출력
# 아니면 구구단 출력 하는 숫자가 아닙니다.

num = int(input("숫자 :"))



if num >= 2 and num <= 9 :
    cnt = 2
    while cnt <= 9:
        print('{} * {} = {}'.format(num, cnt, num*cnt))
        cnt += 1
    else :
        print("구구단끝")

else :
    print("구구단 출력하는 숫자가 아닙니다. ")

