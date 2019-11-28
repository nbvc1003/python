import numpy as np
import matplotlib.pyplot as plt

ar1 = np.zeros((2,3))
print(ar1)

ar2 = np.ones_like(ar1, dtype= int) # 행열의 형태가 ar1과 같고 1로 채워서 만든 행열 타입은 정수
print(ar2, ar2.dtype)

ar3 = np.zeros_like(ar1, dtype= np.float32) # 행열의 형태가 ar1과 같고 0로 채워서 만든 행열 타입은 실수
print(ar3, ar3.dtype)


b1 = np.linspace(0,100,5) # 시작, 끝, 갯수, default 는 끝값 포함
print(b1)
b2 = np.logspace(0.1, 1,10) # Log 의 크기로 분할
print(b2)


plt.plot(b2, 'ro')
# plt.plot(b2, 'g-')
# plt.plot(b2, 'k^:')
plt.show()