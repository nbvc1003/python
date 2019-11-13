
import sys

num1 = int(input('정수 입력 :'))
num2 = int(input('정수 입력 :'))

if num2 != 0 :
    print('{} / {} = {:0.2f}' .format(num1, num2, num1/num2))
    sys.exit(0) # 0 정상종료
else:
    print('0으로 나눌수 없습니다. ')


print('작업 끝')

