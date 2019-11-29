import numpy as np

ar1 = np.array([1,2,3,4,5])
ar2 = ar1[0:3] # 0~3 열
print(ar2)
ar3 = ar1[-2:] # -2열부터 끝까지
print(ar3)
ar4 = ar1[:2] # 처음 부터 2열 앞까지
print(ar4)

br1 = ar1[0:3].copy() # 데이터 복사 (주소가 아닌)
print(br1)
ar1[0] = 77
print(ar2, br1)

