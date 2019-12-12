import matplotlib.pylab as plt
import pandas as pd
# 0 ,1, 2, 3
# eng 98   88   66,  77
# math 94, 77, 88, 66
# 제목 score, eng, math, Legend, grid

plt.title('eng/math Score')
plt.xlabel('no')
plt.ylabel('score')
indexX = pd.Series([0,1,2,3])
eng = pd.Series([98,88,66,77])
math = pd.Series([94,77,88,66])

plt.plot(indexX,eng, label='eng')
plt.plot(indexX,math, label='math')
plt.legend()
plt.grid()
plt.show()