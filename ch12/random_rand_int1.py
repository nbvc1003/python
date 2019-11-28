import numpy as np
import matplotlib.pyplot as plt


# 5~10 정수 10개 균등선택
r1 = np.random.randint(5,10, size=10)
print(r1)

# 0~10 정수 2,5 행열 균등선택
r2 = np.random.randint(0,10, size=(2,5))
print(r2)

data2 = np.random.randint(-100,100, 10000)
plt.hist(data2,bins=100)
plt.show()


