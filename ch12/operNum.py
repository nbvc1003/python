import numpy as np

# 각항목을 2배로
list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = []
for i in list1:
    list2.append(i*2)

print(list2)

arr1 = np.array(list1)
arr2 = arr1 *2
print(arr1, arr2)

# list 형의 경우 *2 일경우 같은 list 내용이 2번 반복 된다. 