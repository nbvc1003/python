import numpy as np

ar = np.array([1,2,3,4])
br = np.array([5,6,7,8])
cr = np.array([-1, 1, 0, -1])

print(ar+br)
print(np.add(ar,br)) # ar + br 과동일
print(np.subtract(ar, br)) # -
print(np.multiply(ar,br)) # = *
print(np.divide(ar,br)) # /
print(np.floor_divide(ar,br)) # 나눈결과를 floor (값중 가장큰값)
print(np.power(ar, br)) # 1**5, 2**6, 3**7, 4**8

print("=========================================")
print(np.maximum(ar,br))
print(np.fmax(ar, br)) # 둘중 큰쪽 위와 동일
print(np.minimum(ar,br))
print(np.fmin(ar,br)) # 둘중 작은쪽  위와 동일
print("=========================================")
print(np.mod(br, ar)) # 나머지값 (%) 와동일
print(np.copysign(ar, cr)) # ar 값을 사용하고 부호(+,-)는 cr것을 사용
print("=========================================")
print("==원소간 비교 ----------------------------")
print(np.greater(ar, br)) # 비교
print(np.greater_equal(ar, br))
print(np.less(ar, br))
print(np.less_equal(ar, br))
print(np.equal(ar, br))
print(np.not_equal(ar, br))
print("=========================================")

print(np.logical_and(ar, br)) # 0은 F, 다른숫자는 T
print(np.logical_or(ar, br))
print(np.logical_xor(ar, br)) # 같으면 True, 다르면 False

cond = [True, False,False,True]
print(np.where(cond, ar, br)) # cond 의 값에 따라 True면 앞쪽, Fasle이면 뒤쪽 값을 선택



















