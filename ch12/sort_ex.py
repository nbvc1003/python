import numpy as np

ar1 = np.array([45,23,67,90])
# 작은순 정렬 (내림차순)
# 오름 차순


print(np.sort(ar1))
print(np.sort(ar1)[::-1])

# 내림차순 인덱스값
# 내림 차순 argsort , argsort를 사용하여 작은순 출력
# argsort사용하여 큰순 출력
br1 = np.argsort(ar1)
print(br1) # 순서값
print(ar1[br1])
print(ar1[-br1])

ar2 = np.array([[2,7,0],[9,1,4],[8,3,5]])

# 상하로 작은 순 상하로 큰 순
print(np.sort(ar2, axis=0))
print(np.sort(ar2, axis=0)[::-1])

# 좌우로 작은순 좌우로 큰순
print(np.sort(ar2, axis=1))
print(np.sort(ar2, axis=1)[::-1])



