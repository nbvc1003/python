import numpy as np

ar = np.arange(1,7).reshape(2,3)
b1 = ar[[1],[2]]
print(b1) # 1행 2열
# fancy index 결과는 배열..

print(ar[[0,1]]) # 0행 1행

b2 = ar[1,2]
print(b2) # 1행 2열  결과는 정수
print(type(b1), type(b2))
cr1 = ar[[1,1]] #ar의 1번행을 두번 가지고 와서 cr1에 배열로 저장
print(cr1)
# cr1 은 주소가 아닌 실제 데이터 영역 확보

cr1[0,1] = 100
print(ar[1]) #
print(cr1)