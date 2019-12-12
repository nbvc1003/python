import matplotlib.pyplot as plt
import pandas as pd
from pylab import savefig

s = pd.Series([84900, 818000, 1756, 292000])
plt.plot(s)
savefig('mypic.png') # 파일저장
plt.show()