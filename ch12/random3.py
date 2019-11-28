import numpy as np
import matplotlib.pyplot as plt

# 평균이 10, 표준편차 1, 갯수 10 ~
arr = np.random.normal(10, 1,size=1000)
# print(arr)

# 데이터가 많을수록 정규분포 그래프를 그린다.
# 가운데가 가장많고 양극단으로 갈수록 적어진다.
plt.hist(arr, bins=100)
plt.show()