import numpy as np

b = np.array([1,2,3,4])
c = np.array([
    [1,2],
    [3,4]
    ])

print(np.prod(b)) # 1*2*3*4
print(np.prod(c, axis=0)) # [1*3, 2*4] -> 열단위로
print(np.prod(c,axis=1)) # [1*2, 2*4]  -> 행단위로

print(np.sum(b)) # 1+2+3+4
print(np.sum(b, keepdims=True)) # 차원을 유지한다. [10]
print(np.sum(c, axis=0)) # [1+3,2+4]
print(np.sum(c, axis=1)) # [1+2, 3+4]




