

import numpy as np
import matplotlib.pyplot as plt
# np.pi = 3.14
# np.sin(), cos, -> 라디안값

# x , y 모두 라디안 값으로 계산된다.

x = np.arange(0, 2 * np.pi, 0.1) # 0 ~ 2pi , 간격 0.1
y = np.sin(x)
plt.plot(x, y)
plt.show()

