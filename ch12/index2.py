import numpy as np


# 21 ~ 29 ar
# 25, 21, 29 출력
# 0행, 마지막 행 출력

ar = np.arange(21, 30).reshape(3,3)

print(ar, ar.shape, ar.dtype, type(ar))

print(ar[1,1])
print(ar[0,0])
print(ar[2,2])

print(ar[0,])
print(ar[-1,-1])