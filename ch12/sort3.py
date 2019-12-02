import numpy as np

ar = np.array([[4,3,5,7],[1,12,11,9],[2,5,1,14]])
print(ar)

print(np.sort(ar)) # default axis = 1 or -1  -> 각 행을 정렬
print(np.sort(ar, axis=0)) # 각 열을 정렬
