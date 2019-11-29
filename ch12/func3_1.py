import numpy as np

b = np.array([1,2,3,4, np.nan])
c = np.array([
    [1,np.nan,2],
    [3,np.nan,4]
    ])

# nanprod : nan = 1, nansum : nan = 0 으로 간주 하고 계산
print(np.nanprod(b)) # 1*2*3*4
print(np.nanprod(c, axis=0)) # [1*3, 2*4] -> 열단위로
print(np.nanprod(c,axis=1)) # [1*2, 2*4]  -> 행단위로

print(np.nansum(b)) # 1+2+3+4
print(np.nansum(b, keepdims=True)) # 차원을 유지한다. [10]
print(np.nansum(c, axis=0)) # [1+3,2+4]
print(np.nansum(c, axis=1)) # [1+2, 3+4]




