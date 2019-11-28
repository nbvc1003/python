import numpy as np

# 0으로 1차원 5개
# 2행3열 1로채워서
# 3행 항등행열
# 위치를 한칸 위로
# 위치를 한칸 아래로
# 1부터 9까지 3행 3열 행열
# 대각선 숫자
# 대각선 한칸위
# 대각선 한칸 아래
# 가비지로 채워진 2,2 행열

arr0 = np.zeros(5)
print(arr0)
arr1 = np.ones((2,3))
print(arr1)
arr2 = np.eye(3, dtype=int) # dtype 을 지정할경우 다른 타입의 데이터를 입력할경우 자동으로 케스팅되어 서 들어감
print(arr2)
arr3 = np.eye(3, k=1)
print(arr3)
arr4 = np.eye(3, k=-1)
print(arr4)

arr5 = np.arange(1,10).reshape(3,3)
print(arr5)
arr6 = np.diag(arr5)
print(arr6)
arr7 = np.diag(arr5, k=1)
print(arr7)
arr8 = np.diag(arr5, k=-1)
print(arr8)

emptyArr = np.empty((2,2))
print(emptyArr)


