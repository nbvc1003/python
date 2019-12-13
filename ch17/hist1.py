import matplotlib.pyplot as plt
import numpy as np

N = 30
np.random.seed(123)
x = np.random.rand(N)
y = np.random.rand(N)
# print(x, y)
size = np.random.rand(N)
color = np.random.rand(N)
# 랜덤하게 적당한 크기로
sizes = np.pi*(15*np.random.rand(N))**2
plt.scatter(x,y, c=color, s=sizes)
plt.show()

