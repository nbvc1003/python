# rand 데이터 1000건 그래프
# randn 1000건 그래프
# randint(1,100, 10) 출력
# 1000그래프 간격 100


import  numpy as np
import matplotlib.pyplot as plt

rd = np.random.rand(1000)
plt.hist(rd)
plt.show()


rd1 = np.random.randn(1000)
plt.hist(rd1)
plt.show()

rd2 = np.random.randint(1,100,size=1000) # 1~100 ,
plt.hist(rd2, bins=100)
plt.show()
