import numpy as np

import matplotlib.pyplot as plt

r1 = np.random.rand(5) # 0포함 [0,1] 0~1실수, 균등분포
r2 = np.random.rand(3,2) # 

print(r1)
print(r2)

# rand : 균등분포
data = np.random.rand(10000)
plt.hist(data, bins=100)
plt.show()

# randn : normal 평균 0, 표준편차
data2 = np.random.randn(10000)
plt.hist(data2, bins=100)
plt.show()

