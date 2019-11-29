# ar 10 19
# 짝수만
# 3의 배수만.
# br 11 30 4행 5열
# cr 0행, 2행
# np.ix_ 사용 1/3행, 0/2열
# br 0행0열 데이터를 45로 변경하고 br, cr 출력하여 확인


import numpy as np

ar = np.arange(10,30)
print(ar)
print(ar[ar%2 == 0])
print(ar[ar%3==0])
br = np.arange(11,31).reshape(4,5)
print(br)
cr = br[[0,2]]
print(cr)
print(br[np.ix_([1,3],[0,2])])
br[0,0] = 45

print(br)
print(cr)
