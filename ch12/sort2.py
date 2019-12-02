import numpy as np

x = np.array([4,2,6,5,1,3,0])
s1 = np.sort(x) #원본 데이터를 복사해서 새로운 배열 생성
print(x)
print(s1)

x.sort() # 원본 자체를 정렬
print(x)


