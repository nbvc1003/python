import numpy as np


ar1 = np.array([0,1,2,3,4,5,6,7,8,9])
ar2 = np.arange(10)

print(ar1)
print(ar2)

ar3 = np.array([[0,1,2,3,4],[5,6,7,8,9]])
ar4 = ar3.reshape(2,5) # 행2 열 5
ar5 = ar2.reshape(2, -1) # 2행으로 하고 열은 자동으로
print(ar3)
print(ar4)
print(ar5)

ar6 = np.linspace(0,1,6) # 시작, 끝, 갯수 (마지막숫자 포함)
print(ar6)
ar7 = np.linspace(0,1,5, endpoint=False) # 마지막 숫자 미포함
print(ar7)
