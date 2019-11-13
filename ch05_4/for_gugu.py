

# 외부로 부터 숫자를 입력 받아서 구구단 출력
# 숫자가 2와 9사이가 아인면 구구단 숫자 아님


while True:
    inputr = input('숫자를 입력하세요 :')
    if inputr.isnumeric():
        num = int(inputr)
        if num == 0:
            break
    else:
        print('is not numbers')
        continue

    if num >= 2 and num <= 9 :
        for i in range(2,10):
            print('{} * {} = {}'.format(num, i, num*i))
    else:
        print('구구단 숫자가 아님')




