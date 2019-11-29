import numpy as np

ar = np.arange(10)
print(ar)

# 범용 함수 : 행열의 각 원소에 적용되는 함수

# 각 원소하나에 적용되는 함수 : 단항 범용 함수
print(np.sqrt(ar)) # 제곱근

x = np.random.randn(4)
y = np.random.randn(4)
print('-------------------------------------------')
print(x)
print(y)

# 이항 범용 함수 : 2개의 행열의 원소를 비교하는 함수
# 같은 위치 끼리 비교해서 큰값으로 추출
print(np.maximum(x,y))
# 같은 위치 끼리 비교해서 작은 값으로
print(np.minimum(x,y))

