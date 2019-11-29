# ar 0 19 (4,5)
# br 0 8 (4,2)
# ar, br 을 좌우로 붙여서 출력 cr 이라 하고 출력
# dr 0 9 (2,5)
# dr ar 을 상하로 붙여서 er 이라고 하고 출력
#
import numpy as np

ar = np.arange(0,20).reshape(4,5)
print(ar)
br = np.arange(0,8).reshape(4,2)
print(br)
cr = np.hstack([ar, br])
print(cr)
print('-----------------------------------------')
dr = np.arange(0,10).reshape(2,5)
print(dr)
er = np.vstack([dr, ar])
print(er)