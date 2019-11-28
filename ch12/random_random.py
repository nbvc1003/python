import numpy as np
import matplotlib.pyplot as plt

r1 = np.random.random((2,4))
print(r1)

# 0~1 실수 1000개  균등
r2 = np.random.random(1000)
plt.hist(r2, bins=10)
plt.show()