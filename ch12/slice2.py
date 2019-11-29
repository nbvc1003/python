import numpy as np

ar1 = np.arange(20).reshape(5,4)
print(ar1)

br1 = np.array(['A','B','C','A','C'])

# 행열 각 원소들과 비교해서 결과를 같은 행열 형태로 리턴
print(br1=='A') # [ True False False  True False]

print(ar1[br1=='A']) # true 인 행만 출력

print(ar1[br1=='A',2]) # true 인 행중에서 2열만

print(ar1[br1=='A', :2]) # true인 행중에서 2열 앞까지만.

# [ True False False  True False]
# True인 행에 100값을 넣어준다.
ar1[br1=='A'] = 100
print(ar1)

