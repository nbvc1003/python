import numpy as np
import matplotlib.pyplot as plt

# ln(x) 결과 값이 이 0.1 ~ 1 사이에 있을때  x 값을 20등분  
lg = np.logspace(0.1, 1, 20)  # 20조각
print(lg)

print(10**0.1, 10**1)
lt = np.linspace(10**0.1, 10**1, 20)
print(lt)


plt.plot(lg,'o')
plt.show()

