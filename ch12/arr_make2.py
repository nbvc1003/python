import numpy as np

# 1~12 를 출력 ,  reshpe {3,4} 출력 shape
# 1 ~ 11를 6조각, 5조각 마지막 제외
arr1 = np.arange(0,12)
arr2 = arr1.reshape(3,4)
# arr2 = arr1.reshape(3,-1) # 위와 동일..
print(arr1, arr1.shape)
print(arr2, arr2.shape)

arr3 = np.linspace(1,11,6)
arr4 = np.linspace(1,11,5,endpoint=False)

print(arr3)
print(arr4)


