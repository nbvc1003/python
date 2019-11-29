import numpy as np

ar1 = np.array([1,2,3])
print(ar1[0], ar1[1], ar1[2])
print(ar1[-1], ar1[-2], ar1[-3])

ar2 = np.array([[1,2],[3,4]])
print(ar2[0][0], ar2[0][1],ar2[1][0],ar2[1][1])

print(ar2[-1][-1], ar2[-2][-2]) #
print(ar2[-1,-1], ar2[-2,-2])  # [1][1] == [1,1] 둘다 같다

# 0행과 , 1행을 전부 출력
print(ar2[0], ar2[1])
