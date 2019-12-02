import numpy as np

ar = np.array([[3,8,2], [9,1,4], [6,7,3]])
print(ar)
print(np.sort(ar, axis=0)) # 열 기준 상하로 작은 순서
print(np.sort(ar, axis=0)[::-1]) # 열기준 상하로 큰순서
print(np.sort(ar, axis=1)) # 행 기준 좌우로 작은 순서
print(np.sort(ar, axis=1)[:,::-1]) # 행 기준 좌우로 큰순서


