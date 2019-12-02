import numpy as np

ar = np.array([90,40,30,78, 30])
print(np.unique(ar)) # 중복 데이터 제거, 정렬

br = np.array([30, 45, 76, 90])
print(np.intersect1d(ar, br)) # 교집합, 공통집합
print(np.union1d(ar,br)) # 홥집합

print(np.in1d(ar, br)) # ar 데이터가 br에 있으면 True, 없으면 False

print(np.setdiff1d(ar,br)) # 차집합 ar에서 br을 빼고 남은 값 (ar - br)

print(np.setxor1d(ar,br)) # 차집합 (ar - br) + (br- ar)  서로 다른 값들만 



