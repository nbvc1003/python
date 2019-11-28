import numpy as np

ar1 = np.array([1,2,3])
print(ar1, ar1.dtype)

ar2 = np.array((['1',2, 3.0]))
print(ar2, ar2.dtype) # U  : 유니코드

ar3 = np.array(([1,2, 3.0]))
print(ar3, ar3.dtype)

# astype 행열의 형변환
ar4 = ar1.astype(np.float)
print(ar4, ar4.dtype)

ar5 = ar1.astype(np.string_)
print(ar5, ar5.dtype) # S 문자형

ar6 = ar1.astype(np.unicode)
print(ar6, ar6.dtype) 