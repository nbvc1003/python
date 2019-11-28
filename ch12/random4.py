import numpy as np
import matplotlib.pyplot as plt
# 평균 0 , 표준편차1인 정규분포 데이터 5건
# 작업을 실행해도 값은 랜덤 값이 나오도록 seed값 고정
# 평균이 100, 표준편차10 정규분포데이터 1000
# 100개 구간으로 나누어서 hist 그래프 출력
np.random.seed(seed=1000)
rm = np.random.normal(0,1,size=5)
print(rm)
rm1 = np.random.normal(100, 10, size=1000)
# print(rm1)
plt.hist(rm1, bins=100)
plt.show()


