import numpy as np
import datetime

li = range(1, 1000000)
s = datetime.datetime.now()

li2 = []
print('리스트 작업 시작 : ', s)
for i in li:
    li2.append(i*2)

s1 = datetime.datetime.now()
print("리스트 작업 완료 : ",s, s1 -s)

ar = np.array(li)
s = datetime.datetime.now()

print('array 작업 시작 : ', s)

arr2 = ar *2
s1 = datetime.datetime.now()
print('array 작업 완료 : ', s, s1 - s)