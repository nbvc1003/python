import numpy as np

ar = np.arange(1,21).reshape(5,4)
print(ar)
print(ar[[1,2]]) # index 가 1~2
print(ar[1:3]) # 행이 1부터 3행

print(ar[[-2, -1]]) # 인덱스가 -2 또는 -1 (-2행 -1행)
print(ar[-2:]) # -2행부터 끝까지..

print(ar[[0,2,4]][:,[0,2]]) # 0,2,4행중에서 행은 전부 열은 0또는 2열

# np.ix_ : 인덱스가 (행, 열).. 위와 같다.
print(ar[np.ix_([0,2,4],[0,2])])

