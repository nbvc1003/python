import numpy as np

ar1 = np.array([1,2,3])
print(ar*2)

ar2 = np.array([[2,3,4],[6,7,9]])
print(ar1 + ar2)
# 행열의 형태가 다를경우 부족한쪽 데이터를 같은 데이터값으로 확장 시켜 동일한 형태로 만들어 연산을 한다.

# 아래와 같이 열의 갯수가 다를경우에는 불가
# ar1 = np.array([1,2])
# ar2 = np.array([[2,3,4],[6,7,9]])

