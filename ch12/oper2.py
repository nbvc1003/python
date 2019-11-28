# ar1: 5 ~7 , ar2: 11 ~12, ar3 :11 ~ 16 (2,3)
# 각각에 3을 곱하여 출력
# 각각을 2로 나누어서 출력
# 각각을 7을 더해서 출력
# ar1, ar2를 +,- ,*,/, %
# ar1, ar3, +,-,*,/, %

import numpy as np

ar1 = np.array([5,6,7])
ar2 = np.array([11,12,13])
ar3 = np.array([[11,12,13],
                [14,15,16]])

print(ar1 + ar2)
print(ar1 - ar2)
print(ar1 * ar2)
print(ar1 / ar2)
print(ar1 % ar2)

print(ar1 + ar3)
print(ar1 - ar3)
print(ar1 * ar3)
print(ar1 / ar3)
print(ar1 % ar3)

