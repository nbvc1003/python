import numpy as np

ar = np.array([10,1,2,3,4])
br = np.array([1.23,4.567,2.76])
cr = np.array([-7,0,2])

print(np.sqrt(ar)) # 루트
print(np.square(ar)) # 제곱
print(np.modf(ar)) # 정수와 소수로 분리 해서 각 다른 배열로
print(np.sign(cr)) # 음수(-1), 0, 양수(+1)

print(np.logical_not(ar <= 2)) # 조건의 논리값을 각배열의 원소와 비교 결과를 배열로
print(ar[np.logical_not(ar <= 2)]) # 조건이 false 인경우에만 값을 가져온다.


