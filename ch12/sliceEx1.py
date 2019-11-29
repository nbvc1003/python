import numpy as np

# ar 21 ~ 40 (5,4)
# 2, 4행
# -3행 부터 끝까지
# 1/3 행중 1/3열
# np.ix_ 로 위와 같이


ar = np.arange(21,41).reshape(5,4)
print(ar)
print(ar[[2,4]])
print(ar[-3:])
print(ar[[1,3]][:,[1,3]])# 행의 인덱스가 1또는 3중에서

print(np.ix_([1,3], [1,3])) # 행의 인덱스가 1또는 3중에서
print(ar[np.ix_([1,3], [1,3])])


# np.ix(a, b) -> a행 과 b열 에 해당하는 행열

