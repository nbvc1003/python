import numpy as np


# ar1은 1~8 2행 4열
# ar1과 같은 행열을 0으로 채우는 정수
# ar1과 같은 행열을 1로 채우는데 float32
# 값과 데이터 타입, shape출력
# 0.1 ~ 1 까지 10개 logspace로 채워서 출력

ar1 = np.arange(1,9).reshape((2,4))
print(ar1)

ar2 = np.zeros_like(ar1, dtype=int)
print(ar2, ar2.shape, ar2.dtype)
ar3 = np.ones_like(ar1, dtype=np.float32)
print(ar3, ar3.shape, ar3.dtype)
ar4 = np.logspace(0.1, 1, 10)
print(ar4)

