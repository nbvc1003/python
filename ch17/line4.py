import matplotlib.pylab as plt
import pandas as pd

# 
s1 = pd.Series([84900, 81800, 71756, 92000])
s2 = pd.Series([80500, 82800, 71736, 90000])
plt.figure(figsize=(10,4)) # 폭 10, 높이 4

plt.plot(s1, label='04-10') # s1 의 이름
plt.plot(s2, label='04-11') # s2 의 이름

plt.title('plot') # 제목
plt.xlabel('index') # x축 라벨
plt.ylabel('stock') # y축 라벨
plt.legend() # 범례
plt.grid() # 격자
plt.show()
