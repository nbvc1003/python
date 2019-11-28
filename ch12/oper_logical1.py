import numpy as np

ar = np.array([1,2,3])
br = np.array([4,2,5])

print(np.equal(ar, br)) # 행열의 같은 위치 의 원소끼리 비교한후 결과를 같은 형식의 행열로 출력

print(np.not_equal(ar,br)) # ar != br
print(np.greater(ar,br)) # ar > br
print(np.greater_equal(ar,br)) # ar >= br
print(np.less(ar,br)) # ar < br
print(np.less_equal(ar,br)) # ar <= br




