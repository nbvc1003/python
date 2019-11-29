import numpy as np

ar = np.arange(10)
print(ar)

index = np.array([True, False,True, False,True, False,True, False,True, False])
print(ar[index]) # True의 위치인 데이터만 가져 온다.
print('--------------------------------------------------')
ar2 = np.arange(15).reshape(5,3)
print(ar2)
print(ar2[[1,2]])
print(ar2[[1,-2]])

print(ar2[[0,2,4]][:,[0,2]])
print(ar2[np.ix_([0,2,4],[0,2])])