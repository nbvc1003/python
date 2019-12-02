import numpy as np

ar = np.array([-4.73,-3.16, 0,1.23, 5.78])

# 정수만 남기고 반올림
# 소수점 1자리 보이게 반올리
# 가까운 정수
# 0에 가까운 쪽으로 정수
# 현재 값보다 크거나 같은 값 중에서 최소
# 소수점 이하 절삭

print(np.around(ar))
print(np.round(ar,1))
print(np.rint(ar))
print(np.fix(ar))
print(np.ceil(ar))
print(np.trunc(ar))
