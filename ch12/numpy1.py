import numpy as np



data1 = [2,3,4,5]
print(data1, type(data1))

# array : 전통적인 의미의 배열 생성
arr1 = np.array([1,2,3,4,5])
print(arr1, type(arr1))
arr2 = np.array(data1)
print(arr2, type(arr2))
print(arr1.shape, arr1.dtype) # dtype 데이터 타입

arr3 = np.array([[1,2,3],[2,3,4]])
print(arr3, arr3.shape) # shape 배열정보

data2 = [2,3,4,5,1.2]
print(data2)

# array 형식은 원소의 데이터 타입이 동일해야 한다. 따라서 큰값의 원소에 맞게변경
arr4 = np.array(data2)
print(arr4, arr4.dtype) 