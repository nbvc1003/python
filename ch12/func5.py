import numpy as np


g = np.array([1,2,4,10,13,20])

# diff차분 
print(np.diff(g)) # 2-1, 4-2, 10-4, 13-10, 20-13
# n=2 : 차분된값의 차분
print(np.diff(g, n=2)) # [2-1, 6-2, 3-6, 7-3]
