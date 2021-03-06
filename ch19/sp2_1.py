from scipy import stats
import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#  시도 횟수 , 성공 확률, cdf (예상 성공수) -> 확률

bi = sp.stats.binom(100, 0.3)

# print(bi.cdf(0)) # 2까지 의 확률 값 합
# print(bi.cdf(10)) # 2까지 의 확률 값 합
# print(bi.cdf(20)) # 10번중 0번 성공 확률
# print(sp.stats.binom(100, 0.3).cdf(30)) # 30번 성공 확률
# print(bi.pmf(30))
# print(bi.cdf(30))

plt.plot(bi.pmf(range(60)), color= 'r')
plt.plot(bi.cdf(range(60)), color='g')

# plt.plot(bi.pmf(range(30)), color= 'r')
# plt.plot(bi.cdf(range(30)), color='g')

# plt.plot(bi.pdf(range(20)))

plt.show()