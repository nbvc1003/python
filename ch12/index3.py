import numpy as np

ar = np.empty((10,5))
print(ar)

for i in range(10):
    ar[i] = i # 행전체에 같은 값을 입력

print(ar)

##
# arr[  [행열의 위치]  ] -> 행열로 결과

# 1행 3행 , 5행 , 7행 을 출력
ar2 = ar[[1,3,5,7]] # 인덱스 배열 , fancy index
print(ar2)

# fancy index 의 결과는 배열..

#         행    열
ar3 = ar[[0,1],[3,4]] # 0행 3열, 1행 4열
print(ar3)

#         행      앞에서 선택한 데이터 중에서 행은 전부 열은 3열만
#               행전부: 열3,4
ar4 = ar[[0,1]][:,[3,4]]
print(ar4)