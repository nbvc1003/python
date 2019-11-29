import numpy as np
# a1 = 1~6 (3,2), a2 = 11~16 (2,3)
# 연산
a1 = np.arange(1,10).reshape(3,3)
a2 = np.arange(11,20).reshape(3,3)
print(a1)
print(a2)
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1/a2)
print(a1**3)

# 행열의 곱셈
print(np.matmul(a1 , a2))


