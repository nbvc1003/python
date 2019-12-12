import matplotlib.pyplot as plt
import pandas as pd

s1 = pd.Series([84900, 81800, 71756, 92000])
s2 = pd.Series([80500, 82800, 71736, 90000])

plt.figure(figsize=(6,4))

# Lw Linewidth 선, 두께 r: RED
plt.plot(s1, label='04-10', lw=3, color='r', linestyle=':')
plt.plot(s2, label='04-11', color='#1DDB16')
plt.xlim(0.0, 4.0)
# ylim : y축을 70000~90000
# y축 표시 최소, 최대
plt.ylim(70000, 90000)

# x축 눈금 0~4 까지 간격이 1
#                 시작, 끝, 간격
plt.xticks(range(0,5,1))
plt.yticks(range(70000, 95000,5000))
plt.grid()
plt.xlabel('index')
plt.ylabel('stock')
plt.legend()
plt.show()