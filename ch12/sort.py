import numpy as np

x = np.array([[2,1,6],
              [0,7,4],
              [5,3,2]])

print(x)
print(np.sort(x,axis=1)) # 행기준 정렬
print(np.sort(x, axis=0)) # 열기준 정렬
print(np.sort(x, axis=0)[::-1]) #  열기준 역정렬


