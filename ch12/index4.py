import numpy as np

# ar : 1~20 4행 5열
# 1행 3열
# 0행 4열, 1행 3열
# 0과 1행 중에서 3열과 4열

ar = np.arange(1, 21).reshape(4,5)
print(ar)
print(ar[1,3])

print(ar[[0,1],[4,3]]) #  == ( ar[0,4], ar[1,3] )

print(ar[[0,1]][:,[3,4]]) #  [0행,1행] [앞에선택된 행중에서만 , [3,4]열]

