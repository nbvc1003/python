import sys
import os
print('정수를 입력하세요')

num = int(input())

if num != 0:
    print('{0:d} / 3 = {1:0.2f}'.format(num, round(num/3),2))

for i in range(len(sys.path)):
    print(sys.path[i])

