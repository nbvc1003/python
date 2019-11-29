import numpy as np

ar = np.array([-4.62, -2.19, 0, 1.57, 3.40, 4.06])

print(np.around(ar)) # 정수까지 반올림
print(np.round(ar,1)) # 반올림 & 소수점 1자리까지 표기
print(np.rint(ar)) # 가장가까운 정수
print(np.fix(ar)) # 0방향으로 가까운 정수

print(np.ceil(ar)) # 현재 값보다 크거나 같은 정수 중에서 가장 작은 값
print(np.floor(ar)) # 현재 값보다 작거나 같은 정수 중에서 가장 작은 값

print(np.trunc(ar)) # 소수점이하를 버린다.


