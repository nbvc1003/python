import numpy as np

b = np.array([1,2,3,4])
c = np.array([
    [1,2],
    [3,4]
    ])

# 누적해서계산

print(np.cumprod(b)) # [1,1*2,1*2*3, 1*2*3*4]
print(np.cumprod(c, axis=0)) # [[1,2][1*3], 2*4], 2*4]] -> 열단위로
print(np.cumprod(c,axis=1)) # [[1, 1*2], [3,3*4]]  -> 행단위로

print(np.cumsum(b)) # 1+2+3+4
print(np.cumsum(c, axis=0)) # [1, 1+3],[2,2+4]
print(np.cumsum(c, axis=1)) # [1, 1+2], [3, 3+4]