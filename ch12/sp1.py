import numpy as np



b1 = np.ones(10) # 크기가 10인 1로 채워진 행열...
print(b1)

b2 = np.zeros((3,3)) # shape 3,3 인 0으로채워진 행열
print(b2)


##------------------------------------------------------------
# eye 항등 행열 , 단위행열
#
ar1 = np.eye(2)
print(ar1)

ar2 = np.eye(2, dtype=int) # 대각선 1 나머지 0
print(ar2)
ar3 = np.eye(3, k=1) # 대각선 1 의 라인을 한칸 위쪽으로 이동
print(ar3)

ar4 = np.eye(3, k=-1) # 대각선 1 의 라인을 한칸 아래로 이동
print(ar4)
ar = np.arange(9).reshape((3,3))
print(ar)
d1 = np.diag(ar) # 대각선 데이터 추출
print(d1)

d2 = np.diag(ar, k=1) # 대각선 1라인 위쪽 추출
print(d2)

d3 = np.diag(ar, k=-1) # 대각선 1라이 아래쪽 추출
print(d3)

# 임의의 값을 가지는 행렬 생성
d4 = np.empty((3,3))
print(d4)

##------------------------------------------------------------