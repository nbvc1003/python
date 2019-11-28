import numpy as np

ar = np.arange(5)
print(ar)
ar2 = ar.reshape((1,5))
print(ar2)
ar3 = ar.reshape((5,1))
print(ar3)

ar4 = ar3[:, np.newaxis] # 열의 차원 증가
print(ar4)


