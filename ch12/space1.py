# 10, 30,  10등분 출력 그래프
# 1, 2  10등분 출력, 그래프
# 1~12  (3,4) 만들어서 출력
# flatten 하여 출력

import numpy as np
import matplotlib.pyplot as plt
arr = np.linspace(10, 30, 10)
plt.plot(arr,'o')
plt.show()
arr1 = np.linspace(1,2,10)
plt.plot(arr1,'o')
plt.show()
arr2 = np.arange(1,13).reshape(3,4)
print(arr2)
arr3 = arr2.flatten()
print(arr3)
